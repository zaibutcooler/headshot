import torch
from torch import nn
from .dataset import Dataset
from .config import Config
from huggingface_hub import PyTorchModelHubMixin
import huggingface_hub

class Model(nn.Module,PyTorchModelHubMixin):
    def __init__(self,config:Config):
        super().__init__()
        self.config = config
        self.num_epoch = config.num_epoch
        self.lr = config.lr
        self.device = config.device

        # TODO start training
        self.layer = nn.Sequential(

        )

        
    def forward(self,x):
        out = self.layer 
        return out

    def save_pretrained(self, name="headshot",username="zaibutcooler"):
        # self.model.save_pretrained(name)
        self.model.push_to_hub(f"{username}/{name}")
        print("Successfully saved the pretrainied")

    def load_pretrained(self, url="zaibutcooler/headshot"):
        self.model = self.gpt.from_pretrained(url)
        print("Successfully loaded the pretrained")

    def huggingface_login(self, token):
        assert token is not None
        huggingface_hub.login(token=token)
        print("Logged in successfully")

    