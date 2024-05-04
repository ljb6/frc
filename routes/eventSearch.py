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

    ampLeverage = go.Figure(go.Bar( x= [eventLeverage, 0.181, 0.198, 0.226, 0.259, 0.261, 0.359, 0.503], y = [event, "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Championship"], orientation="h"))
    ampLeverage.update_layout(title="AMP Leverage",
                              xaxis_title="AMP Leverage (%)",
                              yaxis_title="Events",
                              plot_bgcolor="rgb(243, 244, 246)",
                              paper_bgcolor="rgb(243, 244, 246)")
    ampLeverage.update_traces(texttemplate="%{x}", textposition="outside")
    ampLeveragePlot = ampLeverage.to_html(full_html=False)

    return render_template("eventSearch.html",
                           ampLeveragePlot=ampLeveragePlot)

 