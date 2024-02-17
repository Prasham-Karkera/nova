from flask import Flask, render_template, request
import main
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def convert():
    enterlocation1 = request.form['enterlocation1']
    enterlocation2 = request.form['enterlocation2']
    if enterlocation1:
        str1 = main.set(enterlocation1,1)
    else:
        str2 = main.set(enterlocation2,0)