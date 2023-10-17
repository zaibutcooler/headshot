import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms, datasets
from datasets import load_dataset

data_url = ''

datas = None
labels = None

class FaceDataset(Dataset):
    def __init__(self):
        self.tranforms = transforms.Compose([

        ])
        self.data = datas
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # Load and preprocess the image at the given index
        image = self.data[idx]
        label = self.labels[idx]
        

        image = self.transform(image)
        return image,label