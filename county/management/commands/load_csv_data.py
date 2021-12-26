from csv import DictReader
from django.core.management import BaseCommand

# Import the model 
from county.models import exampleDataNokey, countyMap


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the county data from the CSV file,
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from county.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        '''
        if 
        print(ALREDY_LOADED_ERROR_MESSAGE)
        return
            
            '''
        # Show this before loading the data into the database
        print("Loading county data")


        #Code to load the data into database
        for row in DictReader(open('./csvcounty.csv')):
            print(row)
            countyrow=exampleDataNokey(
                county=row['County'], 
                fips=row['FIPS code'],
                countyseat=row['County seat'],
                est=row['Est.'],
                origin=row['Origin'],
                etymology=row['Etymology'],
                population=row['Population'],
                geometry=countyMap.objects.get(countyfp=int(row['FIPS code'])).geometry,
            )
            countyrow.save()
