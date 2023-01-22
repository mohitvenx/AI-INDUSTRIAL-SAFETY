import ntpath
import torch
from PIL import Image
from helpers import *
#from helpers import draw_box, url_to_img, img_to_bytes


model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/weights/best.pt', force_reload=True) 

#img = Image.open("D:/WABTEC/yolov5/safety_helmets-1/valid/images/ECE160_Dataset690_jpg.rf.c0ba63a107690f72c1b1af0195b410e7.jpg")
#output = model(img)

#print(f'prediction: {output.pred}')

location = './results'

"""

def pipe2(img_path, model):
    print("Detecting Safety Helmet")
    #pred = model.predict(img_path)
    pred = model(img_path)
    out = pred.pred
    return out


def pipe(img_path):
    basename = ntpath.basename(img_path)
    p2 = pipe2(img_path, model)
    #infer on a local image
      #  print(model.predict(img_path, confidence=50, overlap=30).json())
    a = model(img_path)
    a.save(location + '/' + basename)
    #visualize your prediction
  #  model.save(location + '/' + basename)
    result = {'final':'Safety Detection Complete'}
    return result

#pipe("D:/WABTEC/yolov5/safety_helmets-1/valid/images/ECE160_Dataset690_jpg.rf.c0ba63a107690f72c1b1af0195b410e7.jpg")


"""

def predict(img_path):
        # Inference
        basename = ntpath.basename(img_path)

        results = model(img_path)
        # Save image
        results.save(location + '/' + basename, "results")

        result = {'final':'Safety Detection Complete'}
        return result

#predict("D:/WABTEC/yolov5/safety_helmets-1/valid/images/ECE160_Dataset690_jpg.rf.c0ba63a107690f72c1b1af0195b410e7.jpg")
