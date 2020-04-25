#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import send_file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register',methods = ['POST'])
def register():
    result = request.form
    print(result['name'])
    return render_template('registration.html')

@app.route('/static/<file_name>')
def DownLoads(file_name):
    return send_file('./static/img/{}.jpg'.format(file_name), attachment_filename='{}.jpg'.format(file_name))

#Doesn't know if the route must send any static file or only images, and if it's enough to return them or downloads it's mandatory
#@app.route('/static/<file_name>')
#def img(file_name):
    #return send_file('./static/{}'.format(file_name), attachment_filename='{}'.format(file_name))

if __name__ == "__main__":
    app.run(debug=True)