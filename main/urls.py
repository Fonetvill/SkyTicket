from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="home"),
    path('search', views.search_flights, name='search_flights'),
]