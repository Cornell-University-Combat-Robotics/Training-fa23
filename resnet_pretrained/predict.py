# local env: cv
# original article:
# https://learnopencv.com/pytorch-for-beginners-image-classification-using-pre-trained-models/

import torch
from torchvision import transforms
from PIL import Image
from lib.model import model
from lib.core import config
import os
import matplotlib.pyplot as plt

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225])
])

img = Image.open(os.path.join(config.BASE_PATH,
                 "dataset/car.png")).convert('RGB')
img_t = transform(img)

# ---------Display img_t---------------------------------
# def tensor_to_image(tensor):
#     # Convert tensor to numpy array and transpose dimensions
#     img = tensor.numpy().transpose(1, 2, 0)
#     plt.imshow(img)
#     plt.show()
# tensor_to_image(img_t)
# -------------------------------------------------------


batch_t = torch.unsqueeze(img_t, 0)

model = model.resnet
model.eval()

out = model(batch_t)

with open(os.path.join(config.BASE_PATH, 'dataset/imagenet_classes.txt')) as f:
    labels = [line.strip() for line in f.readlines()]

_, index = torch.max(out, 1)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
_, indices = torch.sort(out, descending=True)
print([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])
