from flask import Blueprint, render_template, request
import requests

teamSearch = Blueprint('teamSearch', __name__)

TbaApiKey = "dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw"
TbaApiEndpoint = "https://www.thebluealliance.com/api/v3"
TbaHeaders = {"X-TBA-Auth-Key": TbaApiKey}

@teamSearch.route("/teamsearch")
def index():
    team = request.args.get("team")

    response = requests.get(TbaApiEndpoint + f"/team/frc{team}", headers=TbaHeaders).json()
    print(response)

    teamName = response["nickname"]
    teamCountry = response["country"]
    teamRookieYear = response["rookie_year"]

    return render_template("teamSearch.html", teamName=teamName)