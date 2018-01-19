from django.db import models

# Create your models here.


class AccessData(models.Model):
    county_id = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=100)
    pct_access_2010 = models.FloatField(blank=True, null=True)
    pct_access_2015 = models.FloatField(blank=True, null=True)
    pct_diabetes_2008 = models.FloatField(blank=True, null=True)
    pct_diabetes_2013 = models.FloatField(blank=True, null=True)
    pct_obese_2008 = models.FloatField(blank=True, null=True)
    pct_obese_2013 = models.FloatField(blank=True, null=True)
    grocery_2009 = models.FloatField(blank=True, null=True)
    grocery_2014 = models.FloatField(blank=True, null=True)
    supercenter_2009 = models.FloatField(blank=True, null=True)
    supercenter_2014 = models.FloatField(blank=True, null=True)
    convenience_2009 = models.FloatField(blank=True, null=True)
    convenience_2014 = models.FloatField(blank=True, null=True)
    white_2010 = models.FloatField(blank=True, null=True)
    black_2010 = models.FloatField(blank=True, null=True)
    hispanic_2010 = models.FloatField(blank=True, null=True)
    asian_2010 = models.FloatField(blank=True, null=True)
    amerindian_2010 = models.FloatField(blank=True, null=True)
    hawaiian_2010 = models.FloatField(blank=True, null=True)


    def __str__(self):
        return self.county+','+' '+self.state


class MapData(models.Model):
    variable = models.CharField(max_length=25)
    header_text = models.CharField(max_length=200)
    legend_text = models.CharField(max_length=200)
    lower_bound = models.FloatField()
    upper_bound = models.FloatField()

    def __str__(self):
        return self.variable


class CorrelationData(models.Model):
    variable1 = models.CharField(max_length=20)
    variable2 = models.CharField(max_length=20)
    correlation = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.variable1+' '+self.variable2
