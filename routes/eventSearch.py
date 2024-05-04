from flask import Blueprint, render_template, request, redirect, url_for
import plotly.graph_objects as go
from classes.TbaRequests import TbaRequests

eventSearch = Blueprint('eventSearch', __name__)

tba = TbaRequests("dPeEI571e5LotL4zsavOhgcehtzq0NP7VJaSDOo3gWCMpL1R4riSYvddhBpZZ4Sw")

@eventSearch.route("/eventsearch")
def index():
    event = request.args.get("event") 
    event = "2024" + event

    eventLeverage = tba.getEventsAmpLeverage([event])

    ampLeverage = go.Figure(go.Bar( x= [eventLeverage, 0.25], y = [event, "2024aicf"], orientation="h"))
    ampLeverage.update_layout(title="AMP Leverage", xaxis_title="AMP Leverage (%)", yaxis_title="Events")
    ampLeveragePlot = ampLeverage.to_html(full_html=False)

    return render_template("eventSearch.html",
                           event=event,
                           ampLeveragePlot=ampLeveragePlot)

 