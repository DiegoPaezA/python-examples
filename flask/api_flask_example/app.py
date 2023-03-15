from flask import Flask, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/') # home
def home():
    return 'Hello World!'

@app.route('/carros', methods=['GET']) # endpoint carros
def get_carros():
    return jsonify(Carros)

@app.route('/carros', methods=['POST']) # endpoint carros
def create_carro():
    post_res = request.get_json()
    Carros.append(post_res)
    return jsonify(post_res)
    
    
app.run()