from flask import Flask, render_template, Response, abort, request, send_from_directory

import requests

import os
import subprocess


app = Flask(__name__)




@app.route('/')
def index():


    return render_template('index.html')






if __name__ == '__main__':
    app.run(host='0.0.0.0',port='91', threaded=True, debug=True)
