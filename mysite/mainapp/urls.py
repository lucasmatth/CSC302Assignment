from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name='index'),
    path("day/", views.first_data, name='first_data'),
    path("hour/", views.second_data, name = 'second_data'),
    path("view/", views.third_data, name = "third_data"),
    path("date_til_trend/", views.date_til_trend, name='date_til_trend'),
    ]
urlpatterns += staticfiles_urlpatterns()