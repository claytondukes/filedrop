from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.get("/")
@app.get("/index")
def index():
    return render_template("index.html", filelist=[])

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f"./uploads/{secure_filename(f.filename)}")
    return index()

@app.get('/list')
def show():
    return render_template("index.html", filelist=os.listdir("./uploads"))

@app.get("/uploads/<path:name>")
def getfile(name):
    return send_from_directory("./uploads", name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

