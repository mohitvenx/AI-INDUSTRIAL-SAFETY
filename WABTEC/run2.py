import torch
import PIL 
import models
from PIL import Image
model = torch.load('./yolov5/weights/best.pt')
img = Image.open("D:/WABTEC/yolov5/safety_helmets-1/valid/images/ECE160_Dataset690_jpg.rf.c0ba63a107690f72c1b1af0195b410e7.jpg")
output = model(img)