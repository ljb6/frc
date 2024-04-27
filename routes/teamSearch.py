from flask import Blueprint, render_template, request, redirect, url_for
import requests

teamSearch = Blueprint('teamSearch', __name__)

TbaApiKey = "dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw"
TbaApiEndpoint = "https://www.thebluealliance.com/api/v3"
TbaHeaders = {"X-TBA-Auth-Key": TbaApiKey}

@teamSearch.route("/teamsearch")
def index():
    try:
        team = request.args.get("team")

        responseTeamInfos = requests.get(TbaApiEndpoint + f"/team/frc{team}", headers=TbaHeaders).json()
        responseTeamEvents = requests.get(TbaApiEndpoint + f"/team/frc{team}/events/2024", headers=TbaHeaders).json()

        teamName = responseTeamInfos["nickname"]
        teamCountry = responseTeamInfos["country"]
        teamRookieYear = responseTeamInfos["rookie_year"]
        teamAttendedEvents = ""
        

        for event in responseTeamEvents:
            teamAttendedEvents += event["name"] + "; "

        

        return render_template("teamSearch.html",
                               teamName=teamName,
                               team=team,
                               teamCountry=teamCountry,
                               rookieYear=teamRookieYear,
                               teamAttendedEvents=teamAttendedEvents[:-2])
    except:
        print("Invalid team")
        return redirect(url_for('errorPage.index', team=team))