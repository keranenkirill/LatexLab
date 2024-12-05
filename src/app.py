from flask import flash, jsonify, redirect, render_template, request
from config import app, test_env
from db_helper import reset_db
from repositories.citation_repository import create_citation, get_citations, get_citation
from repositories.citation_repository import del_citation, update_citation
from util import validate_citation_form


@app.route("/")
def index():
    citations = get_citations()
    return render_template("index.html", citations=citations)


@app.route("/new_citation")
def new_citation():
    return render_template("new_citation.html")


@app.route("/delete_citation/<int:citation_id>", methods=["POST"])
def delete_citation(citation_id):
    print(f"Deleting citation with id {citation_id}")
    del_citation(citation_id)
    return redirect("/")


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


@app.route("/edit_citation/<int:citation_id>", methods=["GET"])
def edit_citation(citation_id):
    citation = get_citation(citation_id)
    return render_template("edit_citation.html", citation_id=citation_id, citation=citation)


@app.route("/update_citation/<int:citation_id>", methods=["POST"])
def citation_update(citation_id):
    print(f"Updating citation with id {citation_id}1")
    form_content = request.form.to_dict()
    print(f"Updating citation with id {citation_id}2")
    try:
        validate_citation_form(form_content)
        update_citation(citation_id, form_content)
        print(f"Updated citation with id {citation_id}3")
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return redirect("/edit_citation/<int:citation_id>")


# Route for tests
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({'message': "db reset"})
