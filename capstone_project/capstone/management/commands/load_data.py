from django.core.management.base import BaseCommand
from capstone.models import AccessData

import pandas as pd


# erase the database
def erase_database():
    AccessData.objects.all().delete()



# open xls (pick out relevant data)
def open_data():
    file = r'C:\Users\Jessica\PycharmProjects\pdxcodeguild\capstone_project\capstone\management\commands\food_environment_atlas.xls'
    df1 = pd.read_excel(file, sheetname='ACCESS', converters={'FIPS': str}, usecols=[0, 1, 2, 6, 7])
    df2 = pd.read_excel(file, sheetname='STORES', converters={'FIPS': str}, usecols=[0, 6, 7, 12, 13, 18, 19])
    df3 = pd.read_excel(file, sheetname='HEALTH', converters={'FIPS': str}, usecols=[0, 3, 4, 5, 6])
    df4 = pd.read_excel(file, sheetname='SOCIOECONOMIC', converters={'FIPS': str}, usecols=[0, 3, 4, 5, 6, 7, 8])

    df_join1 = pd.merge(df1, df2, on='FIPS', how='inner')
    df_join2 = pd.merge(df_join1, df3, on='FIPS', how='inner')
    df_join3 = pd.merge(df_join2, df4, on='FIPS', how='inner')


    county_id_column = df_join3['FIPS']
    state_column = df_join3['State']
    county_column = df_join3['County']
    access_column10 = df_join3['PCT_LACCESS_POP10']  # % access for low income population 2010
    access_column15 = df_join3['PCT_LACCESS_POP15']  # % access for low income population 2015
    diabetes_column08 = df_join3['PCT_DIABETES_ADULTS08']  # Estimate age-adjusted percentage age 20+ diabetic 2008
    diabetes_column13 = df_join3['PCT_DIABETES_ADULTS13']  # Estimate age-adjusted percentage age 20+ diabetic 2013
    obese_column08 = df_join3['PCT_OBESE_ADULTS08']  # Estimates age-adjusted percentage persons age 20+ obese 2008
    obese_column13 = df_join3['PCT_OBESE_ADULTS13']  # Estimates age-adjusted percentage persons age 20+ obese 2013
    grocery_column09 = df_join3['GROCPTH09']  # number of grocery stores in county per 1,000 county residents 2009
    grocery_column14 = df_join3['GROCPTH14']  # number of grocery stores in county per 1,000 county residents 2014
    supercenter_column09 = df_join3['SUPERCPTH09']  # number of supercenters in county per 1,000 county residents 2009
    supercenter_column14 = df_join3['SUPERCPTH14']  # number of supercenters in county per 1,000 county residents 2014
    convenience_column09 = df_join3['CONVSPTH09']  # number of convenience stores in county per 1,000 county residents 2009
    convenience_column14 = df_join3['CONVSPTH14']  # number of convenience stores in county per 1,000 county residents 2014
    white_column = df_join3['PCT_NHWHITE10']  # % white population 2010
    black_column = df_join3['PCT_NHBLACK10']  # % black population 2010
    hispanic_column = df_join3['PCT_HISP10']  # % hispanic population 2010
    asian_column = df_join3['PCT_NHASIAN10']  # % asian population 2010
    amerindian_column = df_join3['PCT_NHNA10']  # % american indiana population 2010
    hawaiian_column = df_join3['PCT_NHPI10']  # % hawaiian population 2010

    for i in range(len(access_column10)):
        county_id = county_id_column[i]
        state = state_column[i]
        county = county_column[i]
        pct_access_2010 = access_column10[i]
        pct_access_2015 = access_column15[i]
        pct_diabetes_2008 = diabetes_column08[i]
        pct_diabetes_2013 = diabetes_column13[i]
        pct_obese_2008 = obese_column08[i]
        pct_obese_2013 = obese_column13[i]
        grocery_2009 = grocery_column09[i]
        grocery_2014 = grocery_column14[i]
        supercenter_2009 = supercenter_column09[i]
        supercenter_2014 = supercenter_column14[i]
        convenience_2009 = convenience_column09[i]
        convenience_2014 = convenience_column14[i]
        white_2010 = white_column[i]
        black_2010 = black_column[i]
        hispanic_2010 = hispanic_column[i]
        asian_2010 = asian_column[i]
        amerindian_2010 = amerindian_column[i]
        hawaiian_2010 = hawaiian_column[i]

        all_data = AccessData(county_id=county_id, state=state, county=county, pct_access_2010=pct_access_2010,
                              pct_access_2015=pct_access_2015, pct_diabetes_2008=pct_diabetes_2008,
                              pct_diabetes_2013=pct_diabetes_2013, pct_obese_2008=pct_obese_2008,
                              pct_obese_2013=pct_obese_2013, grocery_2009=grocery_2009, grocery_2014=grocery_2014,
                              supercenter_2009=supercenter_2009, supercenter_2014=supercenter_2014,
                              convenience_2009=convenience_2009, convenience_2014=convenience_2014,
                              white_2010=white_2010, black_2010=black_2010, hispanic_2010=hispanic_2010,
                              asian_2010=asian_2010, amerindian_2010=amerindian_2010, hawaiian_2010=hawaiian_2010)
        all_data.save()

        print(f'{((i/len(access_column10))*100)}%')

# def corr_data():
#     file = r'C:\Users\Jessica\PycharmProjects\pdxcodeguild\capstone_project\capstone\management\commands\food_environment_atlas.xls'
#     df1 = pd.read_excel(file, sheetname='ACCESS', converters={'FIPS': str}, usecols=[0, 1, 2, 6, 7])
#     df2 = pd.read_excel(file, sheetname='STORES', converters={'FIPS': str}, usecols=[0, 6, 7, 12, 13, 18, 19])
#     df3 = pd.read_excel(file, sheetname='HEALTH', converters={'FIPS': str}, usecols=[0, 3, 4, 5, 6])
#     df4 = pd.read_excel(file, sheetname='SOCIOECONOMIC', converters={'FIPS': str}, usecols=[0, 3, 4, 5, 6, 7, 8])
#
#     df_join1 = pd.merge(df1, df2, on='FIPS', how='inner')
#     df_join2 = pd.merge(df_join1, df3, on='FIPS', how='inner')
#     df_join3 = pd.merge(df_join2, df4, on='FIPS', how='inner')
#
#     df_corr = pd.DataFrame(df_join3)
#     x = df_corr['PCT_LACCESS_POP10'].corr(df_corr['PCT_DIABETES_ADULTS13'], method='spearman')
#     y = df_corr['PCT_LACCESS_POP10'].corr(df_corr['PCT_OBESE_ADULTS13'], method='spearman')
#
#     print(x)
#     print(y)


class Command(BaseCommand):

    def handle(self, *args, **options):
        erase_database()
        open_data()
        # corr_data()

