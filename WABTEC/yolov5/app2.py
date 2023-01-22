from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for, flash
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
import openpyxl


ud_weights = "./weights/best.pt"
dt_weights = "./weights/bestbest-helmet-vest.pt"
ti_weights = "./weights/bestbest-vest.pt"

img_dir = 0
app = Flask(__name__)

database={'123456','224466','1234'}

uploads_dir = ('./uploads')

os.makedirs(uploads_dir, exist_ok=True)

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

@app.route("/campagedt")
def campagedt():
    return render_template('test_dt.html')



@app.route("/detectnv", methods=['POST'])
def detectnv():
    if not request.method == "POST":
        return
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    print(video)
    #subprocess.run("ls")
    subprocess.run(['python', 'detect1.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))])

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    obj = secure_filename(video.filename)
    return obj


@app.route("/opencamnv", methods=['GET'])
def opencamnv():
    print("here")
    subprocess.run(['python', 'detect1.py'])
    return "done"
    

@app.route("/detectud", methods=['POST'])
def detectud():
    if not request.method == "POST":
        return
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    print(video)
    #subprocess.run("ls")
    subprocess.run(['python', 'detect2.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename)), 'weights', ud_weights])

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    obj = secure_filename(video.filename)
    return obj


@app.route("/opencamud", methods=['GET'])
def opencamud():
    print("here")
    subprocess.run(['python', 'detect2.py','--weights', ud_weights])
    return "done"

@app.route("/detectti", methods=['POST'])
def detectti():
    if not request.method == "POST":
        return
    video = request.files['video']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    print(video)
    #subprocess.run("ls")
    subprocess.run(['python', 'detect3.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename)), '--weights', ti_weights])

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    obj = secure_filename(video.filename)
    return obj


@app.route("/opencamti", methods=['GET'])
def opencamti():
    print("here")
    subprocess.run(['python', 'detect3.py','--weights', ti_weights ])
    return "done"
    


@app.route('/return-files', methods=['GET'])
def return_file():
    obj = request.args.get('obj')
    loc = os.path.join("runs/detect", obj)
    print(loc)
    try:
        return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
        # return send_from_directory(loc, obj)
    except Exception as e:
        return str(e)

@app.route('/display/<filename>')
def display_video(filename):
    print('display_video filename: ' + filename)
    return redirect(url_for('static/video_1.mp4', code=200))



app.run(host = '0.0.0.0',port = '8000', use_reloader=False)
