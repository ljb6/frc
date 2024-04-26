from flask import Blueprint, render_template, request, redirect, url_for

errorPage = Blueprint('errorPage', __name__)

@errorPage.route("/error")
def index():
    team = request.args.get("team")
    return render_template("errorPage.html", team=team)

    