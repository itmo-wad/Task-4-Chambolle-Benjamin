#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register',methods = ['POST'])
def register():
    result = request.form
    print(result['name'])
    return render_template('registration.html')

#@app.route('/img/<img_name>')
#def img(img_name):
    #response = make_response('./img/python.png')
    #response.mimetype = "image/bmp"
    #return render_template('img.html', myImg=img_name)

if __name__ == "__main__":
    app.run(debug=True)