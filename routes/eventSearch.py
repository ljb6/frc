from flask import Blueprint, render_template, request, redirect, url_for
import plotly.graph_objects as go

eventSearch = Blueprint('eventSearch', __name__)

@eventSearch.route("/eventsearch")
def index():
    event = request.args.get("event")

    inputData = 5
    figure = go.Figure(go.Bar( x= [1, 2, 3], y = [inputData, inputData * 2, inputData  * 3]))
    figure.update_layout(title='Gráfico de Barras', xaxis_title='Eixo X', yaxis_title='Eixo Y')
    plot_div = figure.to_html(full_html=False)

    return render_template("eventSearch.html", event=event, plot_div=plot_div)

 