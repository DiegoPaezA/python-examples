from flask import Flask, request, jsonify
import helper_function as hf
import glob


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# check if file.txt exists if not empty list
list_files = glob.glob('*.txt') # list of files created

@app.route("/") # home page
def home():
    return "Hello, This is the first Task: Create an API with Flask"

# Endpoint to create a file
@app.route("/create_file", methods=["POST"])
def create_file():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    
    if hf.check_file_exists(filename):
        return jsonify(
            Mensagem= "Arquivo ja existe, por favor escolha outro nome",
            Arquivos = list_files)

    list_files.append(filename)
    with open(filename, "w") as f:
        f.write(f"O Arquivo criado foi {filename}")
        
    return jsonify(
        Mensagem= "Lista de Arquivos Criados",
        Arquivos = list_files)
    
# Endpoint to list all the files created   
@app.route("/file_list", methods=["GET"])
def read_filelist():
    if list_files:
        return jsonify(list_files)
    else:
        return jsonify("Nenhum arquivo foi criado")
    
# Endpoint to read a file
@app.route("/read_file", methods=["POST"])
def read_file():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    
    if hf.check_file_exists(filename) == False:
        return jsonify(
            Mensagem= "Arquivo nao existe, por favor escolha outro nome",
            Arquivos = list_files)
        
    with open(filename, "r") as f:
        contents = f.readlines()
        
    return jsonify(
        Mensagem= "Leitura do Arquivo",
        Data = contents)
    
# Endpoint to update a file
@app.route("/update_file", methods=["POST"])
def update_file():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    message = post_res.get("message")
    
    if hf.check_file_exists(filename) == False:
        return jsonify(
            Mensagem= "Arquivo nao existe, por favor escolha outro nome",
            Arquivos = list_files)
    
    with open(filename, "a") as f:
        f.write(f" {message}")
        
    with open(filename, "r") as f:
        contents = f.readlines()
        
    return jsonify(
        Mensagem= "Arquivo Atualizado",
        Data = contents)
    
        
app.run()
