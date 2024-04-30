from flask import Blueprint, render_template, request, redirect, url_for
from classes.TbaRequests import TbaRequests
import requests
import statbotics

teamSearch = Blueprint('teamSearch', __name__)

tba = TbaRequests("dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw")

@teamSearch.route("/teamsearch")
def index():
    try:
        team = request.args.get("team")

        basicInfo = tba.getTeamBasicInfo(team)
        
        return render_template("teamSearch.html",
                               teamName=basicInfo["nickname"],
                               team=team,
                               teamCountry=basicInfo["country"],
                               rookieYear=basicInfo["rookieYear"],
                               teamAttendedEvents=tba.getTeamEvents(team).values())
                               
    except:
        print("Invalid team")
        return redirect(url_for('errorPage.index', team=team))