from flask import Blueprint, render_template, request

teamSearch = Blueprint('teamSearch', __name__)


@teamSearch.route("/teamsearch")
def index():
    team = request.args.get("team")

    return render_template("teamSearch.html", team=team)