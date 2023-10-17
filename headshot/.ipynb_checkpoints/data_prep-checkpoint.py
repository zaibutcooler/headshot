import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms, datasets

data_url = ''


class FaceDataset(Dataset):
    def __init__(self,data,labels,transforms=None):
        self.tranforms = tranforms
        self.data = x_data
        self.labels = y_labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # Load and preprocess the image at the given index
        image = self.data[idx]
        label = self.labels[idx]
        
        if self.transform:
            image = self.transform(image)
        return image,label