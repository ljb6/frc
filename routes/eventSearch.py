from flask import Blueprint, render_template, request, redirect, url_for

eventSearch = Blueprint('eventSearch', __name__)

@eventSearch.route("/eventsearch")
def index():
    event = request.args.get("event")
    return render_template("eventSearch.html", event=event)

 