
from django.views.generic import DetailView
from .models import countyData, countyMap, exampleData, exampleDataNokey, mapGeometry, mapMetaData, mapControl
from django.views.generic.base import TemplateView
from django.core import serializers

class CountyDetailView(DetailView):
    template_name = 'county/county-detail.html'
    model = countyMap




class CountyDataView(TemplateView):
    """ County Data map view."""
    map = countyMap.objects.all()
    data = exampleData.objects.all()
    template_name = "county/county_map.html"

class ExampleDataView(TemplateView):
    map = exampleData.objects.all()
    template_name = "county/county_map.html"
class ExampleDataNokeyView(TemplateView):
    map = exampleDataNokey.objects.all()
    template_name = "county/county_map.html"

class UploadedDataView(TemplateView):
    #map = mapGeometry.objects.all()
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

