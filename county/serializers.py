from rest_framework_gis import serializers

from county.models import countyMap, exampleData, exampleDataNokey, mapMetaData, mapGeometry

class CountyMapGeometrySerializer(serializers.ModelSerializer):
    class Meta:
        #fields = "geometry"
        model = countyMap

class CountyMapSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("statefp", "name")
        geo_field = "geometry"
        model = countyMap
#class ExampleDataSerializer(serializers.GeoFeatureModelSerializer):
class ExampleDataSerializer(serializers.ModelSerializer):
    class Meta:
        countymap = CountyMapGeometrySerializer(many=False)
        fields = ("population", "county", "countymap")
        #geo_field = 'countymap'
        model = exampleData 

class ExampleDataNokeySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("population", "county")
        geo_field = 'geometry'
        model = exampleDataNokey

class UploadedDataSerializer(serializers.GeoFeatureModelSerializer):
    geometry = serializers.GeometryField(precision=2, remove_duplicates=True)
    class Meta:
        fields = ("floatdata", "countyname", "description", "offsetx", "offsety")
        geo_field = 'geometry'
        #lookup_field = 'slug'
        model = mapGeometry
        extra_kwargs = {
                'url': {'lookup_field': 'mapname'}
                }
