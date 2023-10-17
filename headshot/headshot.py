import torch
from torch import nn
from data_prep import FaceDataset

class Headshot(nn.Module):
    def __init__(self):
        super().__init__()
        self.dataset = FaceDataset()
        self.num_epoch = 20

    def forward(self,x):
        pass

    def train(self):
        for epoch in range(self.num_epoch):
            for i,(image,label) in enumerate(self.dataset):
                pass

    def predict(self,image):
        points = self.forward(image)
        

    def load_pretrain(self,name=""):
        pretrained = torch.load(pretrained)
        self.load_state_dict(pretrained)

    