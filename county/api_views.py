"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from county.models import countyMap 
from county.serializers import CountyMapSerializer


class CountyMapViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "geometry"
    filter_backends = (filters.InBBoxFilter,)
    queryset = countyMap.objects.all()
    serializer_class = CountyMapSerializer
