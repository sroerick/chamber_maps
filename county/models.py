from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class countyMap(models.Model):

    statefp = geomodels.CharField(max_length=2, blank=True, null=True)
    countyfp = geomodels.CharField(max_length=3, blank=True, null=True)
    cousubfp = geomodels.CharField(max_length=5, blank=True, null=True)
    cousubns = geomodels.CharField(max_length=8, blank=True, null=True)
    geoid = geomodels.CharField(max_length=10, blank=True, null=True)
    name = geomodels.CharField(max_length=100, blank=True, null=True)
    namelsad = geomodels.CharField(max_length=100, blank=True, null=True)
    lsad = geomodels.CharField(max_length=2, blank=True, null=True)
    classfp = geomodels.CharField(max_length=2, blank=True, null=True)
    mtfcc = geomodels.CharField(max_length=5, blank=True, null=True)
    cnectafp = geomodels.CharField(max_length=3, blank=True, null=True)
    nectafp = geomodels.CharField(max_length=5, blank=True, null=True)
    nctadvfp = geomodels.CharField(max_length=5, blank=True, null=True)
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
