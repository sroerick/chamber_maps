from django.db import models
from django.contrib.gis.db import models as geomodels
from colorfield.fields import ColorField

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
    geometry = geomodels.MultiPolygonField(srid=4326)

    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'counties'

    def __str__(self):
        return self.name


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
    geometry=geomodels.MultiPolygonField(srid=4326)

class mapMetaData(models.Model):
    mapname=models.CharField(max_length=100)
    slug=models.SlugField(max_length=40, null=True, blank=False)
    dateadded=models.DateField(auto_now_add=True)
    datemodified=models.DateField(auto_now=True)
    description=models.CharField(max_length=500)

class mapControl(models.Model):
    lower_limit=models.FloatField()
    upper_limit=models.FloatField()
    color=ColorField()
    mapname=models.ForeignKey('county.mapMetaData', on_delete=models.CASCADE)
