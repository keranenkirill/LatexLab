from flask import flash, jsonify, redirect, render_template, request
from config import app, test_env
from db_helper import reset_db
from entities.citation import Citation
from repositories.citation_repository import create_citation, get_citations
from util import validate_citation_form

@app.route("/")
def index():
    citations = get_citations()
    return render_template("index.html", citations=citations) 

@app.route("/new_citation")
def new_citation():
    return render_template("new_citation.html")

@app.route("/create_citation", methods=["POST"])
def citation_creation():
    form_content = request.form.to_dict()
    try:
        validate_citation_form(form_content)
        create_citation(form_content)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/new_citation")

# Route for tests
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })