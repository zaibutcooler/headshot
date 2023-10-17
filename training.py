import torch
from headshot import Headshot
from headshot import config


num_epochs = 30
out_dir = 'out'
device = 'cuda' if torch.cuda.is_available() else 'cpu'





model = Headshot().to(device)

model.train()