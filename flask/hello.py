"""
@autor: @diripar8
@date: 2023-03-15
@Ref: https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

Este script tiene como objetivo verificar si flask fue instalado correctamente 
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello, World!'
