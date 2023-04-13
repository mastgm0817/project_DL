import streamlit as st
import torch
import requests
from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import Dataset,DataLoader
# from torchvision import models as models
# import cv2
# import torch.nn as nn

# class ImageDataset(Dataset):
#     def __init__(self, csv, train, test):
#         self.csv = csv
#         self.train = train
#         self.test = test
#         self.all_image_names = self.csv[:]['Id']
#         self.all_labels = np.array(self.csv.drop(['Id', 'Genre'], axis=1))
#         self.train_ratio = int(0.85 * len(self.csv))
#         self.valid_ratio = len(self.csv) - self.train_ratio

#         # set the training data images and labels
#         if self.train == True:
#             print(f"Number of training images: {self.train_ratio}")
#             self.image_names = list(self.all_image_names[:self.train_ratio])
#             self.labels = list(self.all_labels[:self.train_ratio])

#             # define the training transforms
#             self.transform = transforms.Compose([
#                 transforms.ToPILImage(),
#                 transforms.Resize((224, 224)),
#                 transforms.RandomHorizontalFlip(p=0.5),
#                 transforms.RandomRotation(degrees=45),
#                 transforms.ToTensor(),
#             ])

#         # set the validation data images and labels
#         elif self.train == False and self.test == False:
#             print(f"Number of validation images: {self.valid_ratio}")
#             self.image_names = list(self.all_image_names[-self.valid_ratio:-10])
#             self.labels = list(self.all_labels[-self.valid_ratio:])

#             # define the validation transforms
#             self.transform = transforms.Compose([
#                 transforms.ToPILImage(),
#                 transforms.Resize((224, 224)),
#                 transforms.ToTensor(),
#             ])

#         # set the test data images and labels, only last 10 images
#         # this, we will use in a separate inference script
#         elif self.test == True and self.train == False:
#             self.image_names = list(self.all_image_names[-10:])
#             self.labels = list(self.all_labels[-10:])

#              # define the test transforms
#             self.transform = transforms.Compose([
#                 transforms.ToPILImage(),
#                 transforms.ToTensor(),
#             ])

    # def __len__(self):
    #     return len(self.image_names)
    
    # def __getitem__(self, index):
    #     image = cv2.imread(f"/content/movie-classifier/Multi_Label_dataset/Images/{self.image_names[index]}.jpg")
    #     # convert the image from BGR to RGB color format
    #     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #     # apply image transforms
    #     image = self.transform(image)
    #     targets = self.labels[index]
        
    #     return {
    #         'image': torch.tensor(image, dtype=torch.float32),
    #         'label': torch.tensor(targets, dtype=torch.float32)
    #     }

def model(pretrained, requires_grad):
    model = models.resnet50(progress=True, pretrained=pretrained)
    # to freeze the hidden layers
    if requires_grad == False:
        for param in model.parameters():
            param.requires_grad = False
    # to train the hidden layers
    elif requires_grad == True:
        for param in model.parameters():
            param.requires_grad = True
    # make the classification layer learnable
    # we have 25 classes in total
    model.fc = nn.Linear(2048, 25)
    return model





def build():
    '''딥러닝 결과 출력 페이지 정의 및 구현'''

    tab_labels = [
        "about Model", "Predict"
    ]
    tab0, tab1 = st.tabs(tab_labels)
   
    with tab0: model_tab() # 팀 소개
    with tab1: pred_tab() # 데이터 설명
    st.subheader("딥러닝 페이지입니다.")


def model_tab():
    option = ["구조", "손실"]
    op_img=st.selectbox("모델 정보", option)
    if op_img=="구조":
        url='whataLIN/structure.png'
    else:
        url='whataLIN/epoch-loss.png'
    image = Image.open(url)
    st.image(image, use_column_width=True)


def pred_tab():

    try:
        image=get_image()
        if image != None:
            st.image(image, caption='업로드된 이미지', use_column_width=True)
            pred_button=st.button("예측")
            if pred_button:
                model = torch.load('whataLIN/Resnet50_final.pth')
                predict(image)
    except Exception as e:
        st.write("구현 아직 못했은ㅎ")
    
    

def get_image():

    from PIL import Image
    uploaded_file = st.file_uploader("포스터 이미지 파일 업로드", type=['jpg', 'jpeg', 'png'])
    image = Image.open(uploaded_file)
    return image
            

def pred_and_show(img):
    model = torch.load('whataLIN/Resnet50_final.pth')

    image = Image.open(img)
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    image = transform(image).unsqueeze(0)

def predict(image):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model2 = model(pretrained=True, requires_grad=False).to(device)
    # learning parameters
    lr = 0.0001
    epochs = 3
    batch_size = 32
    optimizer = optim.Adam(model2.parameters(), lr=lr)
    criterion = nn.BCELoss()
    # read the training csv file
    train_csv = pd.read_csv('whataLIN/train.csv')
    # train dataset
    train_data = ImageDataset(
        train_csv, train=True, test=False
    )
    # validation dataset
    valid_data = ImageDataset(
        train_csv, train=False, test=False
    )
    # train data loader
    train_loader = DataLoader(
        train_data, 
        batch_size=batch_size,
        shuffle=True
    )
    # validation data loader
    valid_loader = DataLoader(
        valid_data, 
        batch_size=batch_size,
        shuffle=False
    )

    train_csv = pd.read_csv('whataLIN/train.csv')
    genres = train_csv.columns.values[2:]
    
    # prepare the test dataset and dataloader

    test_data = ImageDataset(
        train_csv, train=False, test=True
    )
    test_loader = DataLoader(
        test_data,
        batch_size=1,
        shuffle=False
    )

    for counter, data in enumerate(test_loader):
        image, target = data['image'].to(device), data['label']
        # get all the index positions where value == 1
        target_indices = [i for i in range(len(target[0])) if target[0][i] == 1]
        # get the predictions by passing the image through the model
        outputs = net(image)
        outputs = torch.sigmoid(outputs)
        outputs = outputs.detach().cpu()
        sorted_indices = np.argsort(outputs[0])
        best = sorted_indices[-3:]
        string_predicted = ''
        string_actual = ''
        for i in range(len(best)):
            string_predicted += f"{genres[best[i]]}    "
        for i in range(len(target_indices)):
            string_actual += f"{genres[target_indices[i]]}    "
        image = image.squeeze(0)
        image = image.detach().cpu().numpy()
        image = np.transpose(image, (1, 2, 0))
        plt.imshow(image)
        plt.axis('off')
        plt.title(f"PREDICTED: {string_predicted}\nACTUAL: {string_actual}")

        

