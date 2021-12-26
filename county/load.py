import os
from django.contrib.gis.utils import LayerMapping
from county.models import countyMap

county_mapping = {
'statefp' : 'STATEFP',
'countyfp' : 'COUNTYFP',
'countyfp' : 'COUNTYFP',
'countyns' : 'COUNTYNS',
'geoid' : 'GEOID',
'name' : 'NAME',
'namelsad' : 'NAMELSAD',
'lsad' : 'LSAD',
'classfp' : 'CLASSFP',
'mtfcc' : 'MTFCC',
'csafp' : 'CSAFP',
'cbsafp' : 'CBSAFP',
'metdivfp' : 'METDIVFP',
'funcstat' : 'FUNCSTAT',
'aland' : 'ALAND', 
'awater' : 'AWATER', 
'intptlat' : 'INTPTLAT',
'intptlon' : 'INTPTLON',
'geometry' : 'MULTIPOLYGON',
}

county_shp = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'data', 'tl_2021_us_county.shp'),
)

def run(verbose=True):
    lm = LayerMapping(countyMap, county_shp, county_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)
