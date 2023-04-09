from flask import Flask, request, render_template
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/') # home
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
