from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import countyData, countyMap, exampleData, exampleDataNokey, mapGeometry, mapMetaData, mapControl
from django.views.generic.base import TemplateView
from django.core import serializers

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = "county/index.html"

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')
'''
def signin(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
def signup(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
'''
class ExampleDataView(TemplateView):
    map = exampleData.objects.all()
    template_name = "county/county_map.html"
class ExampleDataNokeyView(TemplateView):
    map = exampleDataNokey.objects.all()
    template_name = "county/county_map.html"


class CountyDetailView(DetailView):
    template_name = 'county/county-detail.html'
    model = countyMap

class CountyDataView(TemplateView):
    """ County Data map view."""
    map = countyData
    #map = mapGeometry.objects.all()
    template_name = "county/county_map.html"
   

class UploadedDataView(TemplateView):
    template_name = "county/county_map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mapslug = self.kwargs['slug']
        mapmeta = mapMetaData.objects.get(slug=mapslug)
        mapcontrol = mapControl.objects.filter(mapname_id=mapmeta.id)
        #import ipdb; ipdb.set_trace()
        mapcontroljson = serializers.serialize('json', mapcontrol)
        context['mapname'] = mapmeta.mapname
        context['mapdescription'] = mapmeta.description
        context['slug'] = mapslug
        context['mapcontrol'] = mapcontroljson
        return context

