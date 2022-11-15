from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index')
    path("date_til_trend/", views,date_til_trend, name='date_til_trend')
    ]