from flask import Blueprint, render_template, request, redirect, url_for
import requests
import statbotics

teamSearch = Blueprint('teamSearch', __name__)

tbaApiKey = "dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw"
tbaApiEndpoint = "https://www.thebluealliance.com/api/v3"
tbaHeaders = {"X-TBA-Auth-Key": tbaApiKey}

@teamSearch.route("/teamsearch")
def index():
    try:
        team = request.args.get("team")

        sb = statbotics.Statbotics()

        sbResponseGetTeam = sb.get_team(int(team))
        responseTeamInfos = requests.get(tbaApiEndpoint + f"/team/frc{team}", headers=tbaHeaders).json()
        responseTeamEvents = requests.get(tbaApiEndpoint + f"/team/frc{team}/events/2024", headers=tbaHeaders).json()

        teamName = responseTeamInfos["nickname"]
        teamCountry = responseTeamInfos["country"]
        teamRookieYear = responseTeamInfos["rookie_year"]
        teamAttendedEvents = []
        teamWinrate = sbResponseGetTeam["winrate"]

        for event in responseTeamEvents:
            teamAttendedEvents.append(event["name"])

        return render_template("teamSearch.html",
                               teamName=teamName,
                               team=team,
                               teamCountry=teamCountry,
                               rookieYear=teamRookieYear,
                               teamAttendedEvents=teamAttendedEvents,
                               teamWinrate=(str(teamWinrate * 100))[:5] + "%")
    except:
        print("Invalid team")
        return redirect(url_for('errorPage.index', team=team))