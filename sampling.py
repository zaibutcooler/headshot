import torch
from headshot import Headshot
from headshot import config

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = Headshot().to(device)

pretrained = None

if pretrained:
    model_path = ''
    pass

else:
    model_path = ''
    pass

model.load_state_dict(model_path)

def sample():
    image_path = './interface/images/demo.jpg'

    prediction,image = model.predict_image(image_path)

    print(f"Prediction ->{prediction}")

    return prediction,image