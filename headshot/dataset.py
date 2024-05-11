import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset as HfDataset
from torchvision import transforms, datasets
from datasets import load_dataset

class Dataset(HfDataset):
    def __init__(self):
        self.loaded_data = load_dataset('zaibutcooler/chimp-detection')
        
        self.images = self.loaded_data['image']
        self.labels = self.loaded_data['faces']

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image,label = self.images[idx],self.labels[idx]
        return image,label