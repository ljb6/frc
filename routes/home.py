from flask import Blueprint, render_template, request, redirect, url_for
from classes.TbaRequests import TbaRequests

home = Blueprint('home', __name__)

tba = TbaRequests("dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw")

@home.route("/")
def index():
    try: 
        yearInfo = tba.getYearInfo("2024")

        return render_template("home.html",
                               events=yearInfo["events"]
                               )
                               
    except:
        print("Invalid team")
        return redirect(url_for('errorPage.index'))