from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def first_data(request):
    return render(request, 'firstdata.html')

def second_data(request):
    return render(request, 'seconddata.html')

def third_data(request):
    return render(request, 'thirddata.html')

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
