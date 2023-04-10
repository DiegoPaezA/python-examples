from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/') # home
def index():
    return render_template("index.html")

@app.route('/create_csv', methods=['GET'])
def create_csv():
    path_file = "/volume/data.csv"
    with open(path_file, "w") as f:
        f.write("First Name,Last Name,Email,Phone Number,Address,City,State,Zip Code")
    f.close()
    return "CSV file created"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
