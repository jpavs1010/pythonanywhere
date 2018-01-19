from django.core.management.base import BaseCommand
from capstone.models import MapData
from capstone.models import AccessData
from capstone.models import CorrelationData

import pandas as pd


def erase():
    CorrelationData.objects.all().delete()


def get_attribute(variable_name, data_row):
    if variable_name == 'Access 2010':
        return data_row.pct_access_2010
    elif variable_name == 'Access 2015':
        return data_row.pct_access_2015
    elif variable_name == 'Diabetes 2008':
        return data_row.pct_diabetes_2008
    elif variable_name == 'Diabetes 2013':
        return data_row.pct_diabetes_2013
    elif variable_name == 'Obese 2008':
        return data_row.pct_obese_2008
    elif variable_name == 'Obese 2013':
        return data_row.pct_obese_2013
    elif variable_name == 'Grocery 2009':
        return data_row.grocery_2009
    elif variable_name == 'Grocery 2014':
        return data_row.grocery_2014
    elif variable_name == 'Supercenter 2009':
        return data_row.supercenter_2009
    elif variable_name == 'Supercenter 2014':
        return data_row.supercenter_2014
    elif variable_name == 'Convenience 2009':
        return data_row.convenience_2009
    elif variable_name == 'Convenience 2014':
        return data_row.convenience_2014
    elif variable_name == 'White 2010':
        return data_row.white_2010
    elif variable_name == 'African American 2010':
        return data_row.black_2010
    elif variable_name == 'Hispanic 2010':
        return data_row.hispanic_2010
    elif variable_name == 'Asian 2010':
        return data_row.asian_2010
    elif variable_name == 'American Indian 2010':
        return data_row.amerindian_2010
    elif variable_name == 'Hawaiian 2010':
        return data_row.hawaiian_2010
    return None


def correlate():
    variables = MapData.objects.all()
    data = {}
    for variable in variables:
        data[variable.variable] = []
    for data_row in AccessData.objects.all():
        for variable_name in data:
            datum = get_attribute(variable_name, data_row)
            data[variable_name].append(datum)

    df = pd.DataFrame(data)
    for variable1 in data:
        for variable2 in data:
            # print(va)
            # print(vb)
            # print(df[va].corr(df[vb]))
            # print()
            variable1
            variable2
            correlation = df[variable1].corr(df[variable2])

            all_data = CorrelationData(variable1=variable1, variable2=variable2, correlation=correlation)
            all_data.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        erase()
        correlate()