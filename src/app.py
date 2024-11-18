from flask import render_template
from config import app, test_env

@app.route("/")
def index():
    return render_template("index.html") 