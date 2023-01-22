from roboflow import Roboflow
import ntpath



rf = Roboflow(api_key="ul07DZowk5fawPRlrvWD")
project = rf.workspace().project("hard-hat-workers")
model1 = project.version(13).model


def pipe2(img_path, model):
    print("Detecting Safety Helmet")
    pred = model.predict(img_path)
    return pred
location = './results_final'

def pipe(img_path):
    basename = ntpath.basename(img_path)
    p2 = pipe2(img_path, model1)
    #infer on a local image
    #print(model.predict(img_256, confidence=50, overlap=30).json())
    print(model1.predict(img_path, confidence=50, overlap=30).json())
    #visualize your prediction
    model1.predict(img_path, confidence=50, overlap=20).save(location + '/' + basename)
    result = {'final':'Safety Detection Complete'}
    return result

#pipe("C:\\Users\\Admin\\Downloads\\testimages\\hard_hat_workers1015.png")

#pipe("D:/WABTEC/yolov5/safety_helmets-1/valid/images/ECE160_Dataset690_jpg.rf.c0ba63a107690f72c1b1af0195b410e7.jpg")