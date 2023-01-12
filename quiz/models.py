from django.db import models
import uuid
import json, requests
import pandas as pd

class countryModel(models.Model):
    countryUuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    country     = models.CharField(max_length=250)
    capital     = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country


""" Take API data and put it into a pandas dataframe"""
df = pd.DataFrame(list(zip([i['name'] for i in json.loads(requests.get("https://countriesnow.space/api/v0.1/countries/capital").content)['data']], [i['capital'] for i in json.loads(requests.get("https://countriesnow.space/api/v0.1/countries/capital").content)['data']])),columns=['country', 'capital']).drop_duplicates(subset=['country'])
""" Loop through df and save to local model """
df_position = 0
for i in df['country']:
    """ logic to make sure we don't keep saving the countries in over and over again """
    if len(countryModel.objects.filter(country=str(df['country'].iloc[df_position]))) == 0:
        countryModel.objects.create(country=str(df['country'].iloc[df_position]),capital=str(df['capital'].iloc[df_position])).save()
    df_position += 1