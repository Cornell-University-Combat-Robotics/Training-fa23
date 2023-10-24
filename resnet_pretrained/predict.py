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

# Define the data preprocessing for each data point
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225])
])

# Import in one png image
img = Image.open(os.path.join(config.BASE_PATH,
                 "dataset/car.png")).convert('RGB')
# Preprocess the loaded image
img_t = transform(img)

# ---------Display img_t---------------------------------
# def tensor_to_image(tensor):
#     # Convert tensor to numpy array and transpose dimensions
#     img = tensor.numpy().transpose(1, 2, 0)
#     plt.imshow(img)
#     plt.show()
# tensor_to_image(img_t)
# -------------------------------------------------------

# Convert the preprocessed image to a batch that contains this image
batch_t = torch.unsqueeze(img_t, 0)

# Import the model
model = model.resnet
# Set the model to evaluation mode so that the model will not be unintentionally modified
model.eval()

# Use the model on the batch to get a predicted label
out = model(batch_t)

# Import the labels that were used to train the imported model
with open(os.path.join(config.BASE_PATH, 'dataset/imagenet_classes.txt')) as f:
    labels = [line.strip() for line in f.readlines()]

# Print the top 5 predicted labels
percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
_, indices = torch.sort(out, descending=True)
print([(labels[idx], percentage[idx].item()) for idx in indices[0][:5]])
