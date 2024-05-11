import torch

class Config:
    def __init__(self,num_epoch=20,lr=0.02) -> None:
        self.num_epoch = num_epoch
        self.lr = lr
        self.device ='cuda' if torch.cuda.is_available() else 'cpu'
    
base_config = Config()