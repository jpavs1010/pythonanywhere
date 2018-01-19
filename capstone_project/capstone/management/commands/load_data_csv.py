from django.core.management.base import BaseCommand
from capstone.models import AccessData
import pandas as pd


# erase the database
def erase_database():
    AccessData.objects.all().delete()


path = r'C:\Users\Jessica\PycharmProjects\pdxcodeguild\capstone_project\capstone\management\commands\food_environment_atlas.csv'
# pull out relevant data from csv
def open_data():
    with open(path, 'r') as file:
        text = file.read()

    lines = text.split('\n')

    for i in range(1, len(lines)):
        access_value = lines[i].split(',')
        county_id = access_value[0]
        state = access_value[1]
        county = access_value[2]
        pct_access = access_value[6]
        access_data = AccessData(county_id=county_id, state=state, county=county, pct_access=pct_access)
        access_data.save()
        print(f'{((i/len(lines))*100)}%')


class Command(BaseCommand):

    def handle(self, *args, **options):
        erase_database()
        open_data()
