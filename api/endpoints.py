from api.app import app
from flask import render_template, send_file
from bson import json_util
import os
import codecs


@app.route("/")
def welcome():
    return render_template('main.html')


@app.route("/map/<name_file>")
def show_map(name_file):
    #f=codecs.open(name_file+".html", 'r')
    #return f.read()
    return send_file(f"resources/{name_file}.html")


@app.route("/image/<name_file>")
def show_image(name_file):
    #f=codecs.open(name_file+".html", 'r')
    #return f.read()
    return send_file(f"resources/{name_file}")


