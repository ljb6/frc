from flask import Blueprint, render_template, request, redirect, url_for
from classes.TbaRequests import TbaRequests
import datetime

home = Blueprint('home', __name__)
tba = TbaRequests("")
#year = datetime.date.now().year()

@home.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            event = request.form["event"]
            

            return redirect(url_for("eventSearch.index", event=event))

        yearInfo2024  = tba.getYearInfo("2024")["events"]
        yearInfo2023  = tba.getYearInfo("2023")["events"]
        eventsGrowth = "-" + str(100 - (yearInfo2024 / yearInfo2023 * 100))[:4] + "%"
        teams2024 = 3291
        teamsGrowth = "+" + str((((3291 / 3153) - 1) * 100))[:4] + "%"

        #ampLeverageWeeks = tba.getEventsAmpLeverage()

        return render_template("home.html",
                               events2024=yearInfo2024,
                               eventsGrowth=eventsGrowth,
                               teams2024=teams2024,
                               teamsGrowth=teamsGrowth,
                               impactAward = tba.getEventInfo("2024cmptx")["impactAward"],
                               winners = tba.getEventInfo("2024cmptx")["winners"]
                               )
                               
    except:
        print("Invalid team")
        return redirect(url_for('errorPage.index'))