import os
from django.contrib.gis.utils import LayerMapping
from county.models import countyMap

county_mapping = {
'statefp' : 'STATEFP',
'countyfp' : 'COUNTYFP',
'cousubfp' : 'COUSUBFP',
'cousubns' : 'COUSUBNS',
'geoid' : 'GEOID',
'name' : 'NAME',
'namelsad' : 'NAMELSAD',
'lsad' : 'LSAD',
'classfp' : 'CLASSFP',
'mtfcc' : 'MTFCC',
'cnectafp' : 'CNECTAFP',
'nectafp' : 'NECTAFP',
'nctadvfp' : 'NCTADVFP',
'funcstat' : 'FUNCSTAT',
'aland' : 'ALAND', 
'awater' : 'AWATER', 
'intptlat' : 'INTPTLAT',
'intptlon' : 'INTPTLON',
'geometry' : 'MULTIPOLYGON',
}

county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'tl_2021_17_cousub.shp'),
)

def run(verbose=True):
    lm = LayerMapping(countyMap, county_shp, county_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)
