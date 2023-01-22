import torch
from models.common import DetectMultiBackend
from utils.dataloaders import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, time_sync
import torch.backends.cudnn as cudnn
#Import the necessary libraries and set up the video capture using the cv2 library:
weights = torch.load("D:\\WABTEC\\yolov5\\weights\\best.pt")
device= 'cpu'
device = select_device(device)
model = DetectMultiBackend(weights, device=device)
import cv2
video = cv2.VideoCapture("D:\\WABTEC\\yolov5\\runs\\detect\\exp12\\Top 10 Best Clothing Brands for Construction Workers.mp4")

#Set the frame rate and total number of frames in the video:
frame_rate = video.get(cv2.CAP_PROP_FPS)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

#Iterate through each frame of the video:
while True:
    ret, frame = video.read()

#Use the AIML pytorch object detection model to detect objects in the frame:
    object_detection_results = model(frame)

#Filter the object detection results to only include the desired object:
    filtered_results = [result for result in object_detection_results if result['class'] == 'No Helmet']

#If the filtered results list is not empty, capture and process the frame:
    if filtered_results:
# Capture and process the frame

#Release the video capture and close all windows when finished:
        video.release()
        cv2.destroyAllWindows()




