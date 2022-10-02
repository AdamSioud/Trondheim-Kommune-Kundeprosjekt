from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.coordinates_form, name = 'coordinates-form'),
    path('map', views.maps, name = 'maps'),
]