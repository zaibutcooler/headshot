import torch
from torch import nn
from .data_prep import FaceDataset

class Headshot(nn.Module):
    def __init__(self,num_epoch=20,lr=0.02):
        super().__init__()
        # self.dataset = FaceDataset()
        self.num_epoch = num_epoch
        self.lr = lr
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

        self.layer = nn.Sequential(

        )

        
    def forward(self,x):
        out = self.layer 
        return out

    def train(self):
        loss_fn = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(self.parameters(),lr=self.lr)
        for epoch in range(self.num_epoch):
            for i,(image,label) in enumerate(self.dataset):
                image,label = image.to(self.device),label.to(self.device)

                optimizer.zero_grad()
                
                output = self(image)
                loss = loss_fn(output,label)
                loss.backward()
                optimizer.step()
            print(f"epoch {epoch} loss:{loss.item()}")
                

    def predict_image(self,image):
        points = self.forward(image)
        
    def predict_video(self,video):
        pass

    def load_pretrain(self,name=""):
        pretrained = torch.load(pretrained)
        self.load_state_dict(pretrained)

    