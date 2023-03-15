from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

list_files = []

@app.route("/") # home page
def home():
    return "Create File API"

@app.route("/create_file", methods=["POST"])
def create_file():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    list_files.append(post_res)
    with open(filename, "w") as f:
        f.write(f"O Arquivo criado foi {filename}")
        
    return jsonify(
        Mensagem= "Lista de Arquivos Criados",
        Data = list_files)
    
@app.route("/file_list", methods=["GET"])
def read_filelist():
    return jsonify(list_files)

@app.route("/read_file", methods=["POST"])
def read_file():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    with open(filename, "r") as f:
        contents = f.readlines()
        
    return jsonify(
        Mensagem= "Leitura do Arquivo",
        Data = contents)

@app.route("/update_file", methods=["POST"])
def update_file():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    message = post_res.get("message")
    
    with open(filename, "a") as f:
        f.write(f" {message}")
        
    with open(filename, "r") as f:
        contents = f.readlines()
        
    return jsonify(
        Mensagem= "Arquivo Atualizado",
        Data = contents)
    
        
app.run()
