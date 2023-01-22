from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for,send_from_directory, flash
from werkzeug.utils import secure_filename
import os
import subprocess
import openpyxl
import ntpath
from os.path import join, dirname, realpath

he_weights = "./weights/best.pt"
he_ve_weights = "./weights/best-helmet-vest.pt"
ve_weights = "./weights/best-vest.pt"

app = Flask(__name__)

database={'123456','224466','1234', 'wabtec-exceed', "WABTEC2.0"}

uploads_dir = ('./uploads')
RESULTS_FOLDER_IMG = join(dirname(realpath('save.jpg')),'./yolov5/runs/detect/video-results')
app.config['RESULTS_FOLDER_IMG'] = RESULTS_FOLDER_IMG
RESULTS_FOLDER_VID = join(dirname(realpath('save.mp4')),'./yolov5/runs/detect/video-results')
app.config['RESULTS_FOLDER_VID'] = RESULTS_FOLDER_VID

app.config['uploads_dir'] = uploads_dir
app.secret_key='key'

ALLOWED_EXTENSIONS = {'png', 'PNG', 'jpg', 'JPG', 'jpeg', 'JPEG', 'gif', 'GIF','mp4', 'MP4'}

os.environ["FLASK_ENV"] = "development"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def login_page():
    #return render_template('base.html')
    return render_template('login.html')

@app.route('/form_login',methods=['POST'])
def form_login():
    name1=request.form['SECURITY PIN']
    if name1 in database:
        return render_template('index.html',name=name1)
    else:
        return render_template('login.html',info='Invalid User')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/campage")
def campage():
    return render_template('test.html')

@app.route("/campageuav")
def campageuav():
    return render_template('test_uav.html')

@app.route("/campageti")
def campageti():
    return render_template('test_ti.html')

@app.route("/detectnv", methods=['POST', 'GET'])
def detectnv():
    if not request.method == "POST":
        return
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    print(video)
    #subprocess.run("ls")
    subprocess.run(['python', './detect1.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))])

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    filename = secure_filename(video.filename)
    #return obj
    return render_template("./output.html", filename = filename)



@app.route("/opencamnv", methods=['GET'])
def opencamnv():
    print("here")
    subprocess.run(['python', './detect1.py'])
    return "done"
    

@app.route("/detectud", methods=['POST'])
def detectud():
    if not request.method == "POST":
        return
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    print(video)
    #subprocess.run("ls")
    subprocess.run(['python', 'detect2.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename)), '--weights', he_ve_weights])

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    obj = secure_filename(video.filename)
    return obj


@app.route("/opencamud", methods=['GET'])
def opencamud():
    print("here")
    subprocess.run(['python', 'detect2.py','--weights', he_ve_weights])
    return "done"

@app.route("/detectti", methods=['POST', 'GET'])
def detectti():
    if request.method == "POST":
        video = request.files['video']
        video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
        print(video)
        #subprocess.run("ls")
        subprocess.run(['python', 'detect3.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename)), '--weights', ve_weights])

        # return os.path.join(uploads_dir, secure_filename(video.filename))
        obj = secure_filename(video.filename)
        return obj
    if request.method == "GET":
        return render_template('output.html', filename = obj)


@app.route("/opencamti", methods=['GET'])
def opencamti():
    print("here")
    subprocess.run(['python', 'detect3.py','--weights', ve_weights ])
    return "done"
    



@app.route('/return_files', methods=['GET'])
def return_files():
    obj = request.args.get('obj')
    loc = os.path.join("./yolov5/runs/detect/video-results", obj)
    print(loc)
    try:
        #return send_file(os.path.join(".yolov5/runs/detect/video-results/", obj), as_attachment=True)
        return send_file("./yolov5/runs/detect/video-results/" + obj)
    except Exception as e:
        return str(e)

@app.route('/')
def assess():
   return render_template("index.html", result=None, scroll='third')

@app.route('/results/<filename>')
def send_file(filename):
    #filename = ntpath.basename(filename)
    loc = os.path.join("./yolov5/runs/detect/video-results/", filename)
    return send_from_directory(app.config['RESULTS_FOLDER'], filename)

@app.route('/alert')
def alert():
    return render_template('output.html')

@app.route('/send_images/<filename>', methods = ['GET', 'POST'])
def send_images(filename):
    #obj = request.args.get('obj')
    #obj = ntpath.basename(obj)
    #filename = "./yolov5/runs/detect/video-results/" + obj
    filename = ntpath.basename(filename)
    return send_from_directory(RESULTS_FOLDER_IMG,filename)
    
@app.route('/videos/<filename>')
def send_videos(obj):
    obj = ntpath.basename(obj)
    filename = "./yolov5/runs/detect/video-results/" + obj
    return send_from_directory(app.config['RESULTS_FOLDER_VID'], obj, as_attachment = True)



app.run(host = '0.0.0.0',port = '8000', use_reloader=False)
