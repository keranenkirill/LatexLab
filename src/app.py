from flask import jsonify, render_template
from config import app, test_env
from db_helper import reset_db

@app.route("/")
def index():
    return render_template("index.html") 

# Route for tests
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })