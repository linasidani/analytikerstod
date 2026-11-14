from flask import Flask, render_template, request
from service import search

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
