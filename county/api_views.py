"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from county.models import countyMap, exampleData, exampleDataNokey, mapGeometry
from county.serializers import ExampleDataSerializer, CountyMapSerializer, ExampleDataNokeySerializer, UploadedDataSerializer
from rest_framework import generics


class CountyMapViewSet(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = "geometry"
    filter_backends = (filters.InBBoxFilter,)
    queryset = countyMap.objects.all()
    serializer_class = CountyMapSerializer


class ExampleDataViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (filters.InBBoxFilter,)
    queryset = exampleData.objects.all().values('county', 'population', 'countymap')
    #bbox_filter_field = "countymap"
    serializer_class = ExampleDataSerializer

class ExampleDataNokeyViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (filters.InBBoxFilter,)
    queryset = exampleDataNokey.objects.all().values('county', 'population', 'geometry')
    bbox_filter_field = "geometry"
    serializer_class = ExampleDataNokeySerializer

class UploadedDataAPIView(generics.ListAPIView):
    serializer_class = UploadedDataSerializer
    def get_queryset(self):
        queryset = mapGeometry.objects.all().values('countyname', 'floatdata', 'description','geometry', 'mapname')
        mapname = self.kwargs['slug']
<<<<<<< HEAD
        return mapGeometry.objects.filter(mapname__slug=mapname).geometry.simplify
=======
        return mapGeometry.objects.filter(mapname__slug=mapname)
>>>>>>> c44398f262d9c406063b06406b6841820f33d4be
        #return mapGeometry.objects.all()

'''
class UploadedDataViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (filters.InBBoxFilter,)
    queryset = mapGeometry.objects.all().values('countyname', 'floatdata', 'description','geometry', 'mapname')

    lookup_field = 'mapname'
    bbox_filter_field = "geometry"
    serializer_class = UploadedDataSerializer
'''
