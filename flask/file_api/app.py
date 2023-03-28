from flask import Flask, request, jsonify, render_template
import helper_function as hf
from dummy_data import images
import glob
import random
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# check if files folder exists if not create it
if(hf.check_file_exists("files")==False):
    os.mkdir("files")
    
# check if file.txt exists if not empty list
list_files = glob.glob('files/*') # list of files created


@app.route("/") # home page
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)

# Endpoint to create a file
@app.route("/create_file", methods=["POST"])
def create_file():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    filename_path = "files/" + filename
    
    if hf.check_file_exists(filename_path):
        return jsonify(
            Mensagem= "Arquivo ja existe, por favor escolha outro nome",
            Arquivos = list_files)

    list_files.append(filename)
    with open(filename_path, "w") as f:
        print(f"O Arquivo criado foi {filename}")
    f.close()    
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
    filename_path = "files/" + filename
    
    if hf.check_file_exists(filename_path) == False:
        return jsonify(
            Mensagem= "Arquivo nao existe, por favor escolha outro nome",
            Arquivos = list_files)
        
    with open(filename_path, "r") as f:
        contents = f.readlines()
    f.close()
        
    return jsonify(
        Mensagem= "Leitura do Arquivo",
        Data = contents)
    
# Endpoint to update a file
@app.route("/update_file", methods=["POST"])
def update_file():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    message = post_res.get("message")
    mode = post_res.get("mode")
    filename_path = "files/" + filename
    
    if hf.check_file_exists(filename_path) == False:
        return jsonify(
            Mensagem= "Arquivo nao existe, por favor escolha outro nome",
            Arquivos = list_files)
    else:
        if hf.check_file_type(filename) == "csv":
            if mode == "w":
                hf.add_data_to_csv(filename,data=message, mode="w")
                contents = "Arquivo CSV prenchido"
            else:
                hf.add_data_to_csv(filename,data=message, mode="a")
                contents = "Arquivo CSV atualizado"
            
        elif hf.check_file_type(filename) == "txt":
            with open(filename_path, "a") as f:
                f.write(f" {message}")
            f.close()
            with open(filename_path, "r") as f:
                contents = f.readlines()
            f.close()
                
    return jsonify(Mensagem= "Arquivo Atualizado",
                   Data = contents)
    
@app.route("/filter_data", methods=["POST"])
def filter_data():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    filter = post_res.get("filter")
    filename_path = "files/" + filename
    
    if hf.check_file_exists(filename_path) == False:
        return jsonify(
            Mensagem= "Arquivo nao existe, por favor escolha outro nome",
            Arquivos = list_files)
    else:
        if hf.check_file_type(filename) == "csv":
           column = filter.get("column")
           value = filter.get("value")
           contents = hf.filter_csv(filename, column, value)
 
            
        elif hf.check_file_type(filename) == "txt":
            contents = "A funcao nao esta disponivel para arquivos txt"
                
    return contents

@app.route("/filter_range", methods=["POST"])
def filter_range():
    post_res = request.get_json()
    filename = post_res.get("file_name")
    filter = post_res.get("filter")
    filename_path = "files/" + filename
    
    if hf.check_file_exists(filename_path) == False:
        return jsonify(
            Mensagem= "Arquivo nao existe, por favor escolha outro nome",
            Arquivos = list_files)
    else:
        if hf.check_file_type(filename) == "csv":
           value1 = filter.get("value1")
           value2 = filter.get("value2")
           contents = hf.filter_range_csv(filename, value1, value2)
 
            
        elif hf.check_file_type(filename) == "txt":
            contents = "A funcao nao esta disponivel para arquivos txt"
                
    return contents
    
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
