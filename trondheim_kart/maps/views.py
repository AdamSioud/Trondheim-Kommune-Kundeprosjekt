from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Coordenadas
from .forms import *
import folium

# Create your views here.

def coordinates_form(request):
    coordinates = Coordenadas.objects.all()
    form = CoordinatesForm()

    if request.method == 'POST':
        form = CoordinatesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("maps")
    context = {
        'coordinates': coordinates,
        'form' : form,
    }
    return render(request, 'maps/maps_form.html', context)

def maps(request):
    coordenadas = list(Coordenadas.objects.values_list('lat','lon'))[-1]

    map = folium.Map(coordenadas)
    folium.Marker(coordenadas).add_to(map)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
    folium.LayerControl().add_to(map)


    map = map._repr_html_()
    context = {
        'map': map,

    }
    return render(request, 'maps/maps.html', context)