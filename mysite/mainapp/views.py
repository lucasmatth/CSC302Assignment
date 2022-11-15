from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return HttpResponse("I am running! I'm gonna talk to a database!")

def date_til_trend(request):
    stats_f = open("../../data analysis/days til trend/data")
    stats = json.load(data_f)
    graph_f = open("../../data analysis/days til trend/days_plot", "rb")
    graph = graph_f.read()
    data = {
        "stats": stats,
        "graph": graph
        }
    response = HttpResponse(data, content_type='application/json')
    return response
