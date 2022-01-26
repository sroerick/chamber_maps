from django.db import models
from django.contrib.gis.db import models as geomodels
from colorfield.fields import ColorField
from django.utils.html import format_html
from django.urls import reverse 

# Create your models here.

class countyMap(models.Model):

    statefp = geomodels.CharField(max_length=2, blank=True, null=True)
    countyfp = geomodels.IntegerField(blank=True, null=True, unique=True)
    countyns = geomodels.CharField(max_length=8, blank=True, null=True)
    geoid = geomodels.CharField(max_length=55555, blank=True, null=True)
    name = geomodels.CharField(max_length=100, blank=True, null=True)
    namelsad = geomodels.CharField(max_length=100, blank=True, null=True)
    lsad = geomodels.CharField(max_length=2, blank=True, null=True)
    classfp = geomodels.CharField(max_length=2, blank=True, null=True)
    mtfcc = geomodels.CharField(max_length=5, blank=True, null=True)
    csafp = geomodels.CharField(max_length=3, blank=True, null=True)
    cbsafp = geomodels.CharField(max_length=5, blank=True, null=True)
    metdivfp = geomodels.CharField(max_length=5, blank=True, null=True)
    funcstat = geomodels.CharField(max_length=1, blank=True, null=True)
    aland = geomodels.BigIntegerField()
    awater = geomodels.BigIntegerField()
    intptlat = geomodels.CharField(max_length=11, blank=True, null=True)
    intptlon = geomodels.CharField(max_length=12, blank=True, null=True)
    offsetx = geomodels.FloatField(default=0)
    offsety = geomodels.FloatField(default=0)
    geometry = geomodels.MultiPolygonField(srid=4326)

    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'counties'

    def __str__(self):
        return self.name

class stateTiger(models.Model):
    region = geomodels.CharField(max_length=2)
    division = geomodels.CharField(max_length=2)
    statefp = geomodels.CharField(max_length=2)
    statens = geomodels.CharField(max_length=8)
    geoid = geomodels.CharField(max_length=2)
    stusps = geomodels.CharField(max_length=2)
    name = geomodels.CharField(max_length=100)
    lsad = geomodels.CharField(max_length=2)
    mtfcc = geomodels.CharField(max_length=5)
    funcstat = geomodels.CharField(max_length=1)
    aland = geomodels.BigIntegerField()
    awater = geomodels.BigIntegerField()
    intptlat = geomodels.CharField(max_length=11)
    intptlon = geomodels.CharField(max_length=12)
    offsetx = geomodels.FloatField(default=0)
    offsety = geomodels.FloatField(default=0)
    geom = geomodels.MultiPolygonField(srid=4326)


class countyData(models.Model):
    county=models.CharField(max_length=100)
    data = models.FloatField()
    collection=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class exampleData(models.Model):
    county=models.CharField(max_length=100)
    fips=models.CharField(max_length=5)
    countyseat=models.CharField(max_length=100)
    est=models.FloatField()
    origin=models.CharField(max_length=500)
    etymology=models.CharField(max_length=500)
    population=models.FloatField()
    countymap=models.ForeignKey('county.countyMap', on_delete=models.CASCADE)
class exampleDataNokey(models.Model):
    county=models.CharField(max_length=100)
    fips=models.CharField(max_length=5)
    countyseat=models.CharField(max_length=100)
    est=models.FloatField()
    origin=models.CharField(max_length=500)
    etymology=models.CharField(max_length=500)
    population=models.FloatField()
    geometry=geomodels.MultiPolygonField(srid=4326)

class mapGeometry(models.Model):
    mapname=models.ForeignKey('county.mapMetaData', on_delete=models.CASCADE)
    countyname=models.CharField(max_length=100)
    fips=models.CharField(max_length=5)
    floatdata=models.FloatField()
    description=models.CharField(max_length=500, null=True, blank=True)
    offsetx = geomodels.FloatField(default=0)
    offsety = geomodels.FloatField(default=0)
    geometry=geomodels.MultiPolygonField(srid=4326)

class mapMetaData(models.Model):
    mapname=models.CharField(max_length=100)
    slug=models.SlugField(max_length=40, null=True, blank=False)
    dateadded=models.DateField(auto_now_add=True)
    datemodified=models.DateField(auto_now=True)
    description=models.CharField(max_length=500)
    lonlat=models.CharField(max_length=500, default="-88.528,39.938")
    zoom=models.FloatField(default=6)
    declutter=models.BooleanField(default=True)
    make_private=models.BooleanField(default=True)
    show_osm=models.BooleanField(default=True)
    toggle_value_display=models.BooleanField(default=True)
    line_color=ColorField()
    line_weight=models.IntegerField(default=3)
    font_size=models.IntegerField(default=8)
    font_color=ColorField(default="#000000")
    font_inlay_color=ColorField()
    font_inlay_weight=models.IntegerField(default=3)

    class Meta:
        verbose_name = "Map"
        verbose_name_plural = "Maps"
    
    def get_absolute_url(self):
        #return "/map/%i/" % self.slug
        return reverse('map', kwargs={'slug': self.slug})


class mapControl(models.Model):
    lower_limit=models.FloatField()
    upper_limit=models.FloatField()
    color=ColorField()
    mapname=models.ForeignKey('county.mapMetaData', on_delete=models.CASCADE)



