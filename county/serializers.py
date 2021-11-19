from rest_framework_gis import serializers

from county.models import countyMap

class CountyMapSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        fields = ("cousubfp", "name")
        geo_field = "geometry"
        model = countyMap
