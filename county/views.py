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



def OLMapViewTwo(request, slug):
    mapslug = slug
    mapmeta = mapMetaData.objects.get(slug=mapslug)
    mapcontrol = mapControl.objects.filter(mapname_id=mapmeta.id)
    mapcontroljson = serializers.serialize('json', mapcontrol)
    context={}
    context['mapname'] = mapmeta.mapname
    context['mapdescription'] = mapmeta.description
    context['maplonlat'] = mapmeta.lonlat
    context['mapzoom'] = mapmeta.zoom
    context['mapdeclutter'] = mapmeta.declutter
    context['linecolor'] = str(mapmeta.line_color)
    context['fontcolor'] = str(mapmeta.font_color)
    context['fontinlaycolor'] = str(mapmeta.font_inlay_color)
    context['fontinlayweight'] = str(mapmeta.font_inlay_weight)
    context['lineweight'] = str(mapmeta.line_weight)
    context['fontsize'] = mapmeta.font_size
    context['slug'] = mapslug
    context['mapcontroljson'] = mapcontroljson
    context['mapcontrol'] = mapcontrol
    if (mapmeta.make_private == True) and not request.user.is_authenticated:
         return redirect('/accounts/login/?next=%s' % request.path)
    else:
        return render(request, "county/olmap.html", context)

    

class OLMapView(TemplateView):
    template_name = "county/olmap.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mapslug = self.kwargs['slug']
        mapmeta = mapMetaData.objects.get(slug=mapslug)
        mapcontrol = mapControl.objects.filter(mapname_id=mapmeta.id)
        context['mapname'] = mapmeta.mapname
        context['mapdescription'] = mapmeta.description
        context['mapdeclutter'] = mapmeta.declutter
        context['slug'] = mapslug
        context['mapcontrol'] = mapcontroljson
        return context

