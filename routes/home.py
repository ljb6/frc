from flask import Blueprint, render_template, request, redirect, url_for

home = Blueprint('home', __name__)

@home.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            team = request.form['team']

            print("teste", team)

            return redirect(url_for('teamSearch.index', team=team))
    except:
        print("Invalid team")
    
    return render_template("home.html")

    