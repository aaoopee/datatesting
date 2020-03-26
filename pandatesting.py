
import pandas
import os
from geopy.geocoders import ArcGIS
nom = ArcGIS()

print(os.listdir())

df_excel = pandas.read_excel("original.xlsx", sheet_name=0)

print(df_excel)

