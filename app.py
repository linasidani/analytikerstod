from flask import Flask, render_template, request, redirect, url_for
from service import search
from models import add_person, add_organisation, add_log
app = Flask(__name__)       

@app.route("/")             
def index(): 
    q = request.args.get("q", "")

    results = search (q) if q else []

    return render_template(
        "search.html",
        q=q,
        results=results
    )            
  
@app.route("/add-person", methods=["POST"])
def create_person():
    name = request.form.get("person_name", "").strip()
    notes = request.form.get("person_notes", "").strip()

    if name:
        add_person(name, notes)
        add_log(f"Added person: {name}")

    return redirect(url_for("index"))


@app.route("/add-organisation", methods=["POST"])
def create_organisation():
    name = request.form.get("organisation_name", "").strip()
    country = request.form.get("organisation_country", "").strip()

    if name:
        add_organisation(name, country)
        add_log(f"Added organisation: {name}")

    return redirect(url_for("index"))