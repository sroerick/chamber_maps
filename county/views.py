
from django.views.generic import DetailView
from .models import countyData, countyMap
from django.views.generic.base import TemplateView

class CountyDetailView(DetailView):
    """
        City detail view.
    """
    template_name = 'county/county-detail.html'
    model = countyMap




class CountyDataView(TemplateView):
    """ County Data map view."""

    template_name = "county/county_map.html"
