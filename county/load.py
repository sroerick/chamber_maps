import os
from django.contrib.gis.utils import LayerMapping
from county.models import countyMap, stateTiger

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

statefips_mapping = {
    'region': 'REGION',
    'division': 'DIVISION',
    'statefp': 'STATEFP',
    'statens': 'STATENS',
    'geoid': 'GEOID',
    'stusps': 'STUSPS',
    'name': 'NAME',
    'lsad': 'LSAD',
    'mtfcc': 'MTFCC',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geom': 'MULTIPOLYGON',
}


county_shp = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'data', 'tl_2021_us_county.shp'),
)

state_shp = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../statedata', 'tl_2017_us_state.shp'),
)

def run(verbose=True):
    #county_lm = LayerMapping(countyMap, county_shp, county_mapping, transform=True)
    #countylm.save(strict=True, verbose=verbose)
    state_lm = LayerMapping(stateTiger, state_shp, statefips_mapping, transform=True)
    state_lm.save(strict=True, verbose=verbose)
