#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import shapely
from shapely.geometry import Point, mapping, shape
from shapely.ops import cascaded_union
from fiona import collection
t = r'C:\Users\zandb\OneDrive\Documents\Northeastern\Classwork\GIS 6345 Geospatial Programming\Week 7\Assignment\King_County_Metro_Transit_Centers___transit_centers_point.csv'


# In[2]:


t


# In[3]:


with open(t, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


# In[4]:


{'lat': '41.88', 'lon': '-87.63', 'name': 'Chicago'}
{'lat': '39.101', 'lon': '-94.584', 'name': 'Kansas City'}


# In[5]:


with open(t, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        point = Point(float(row['LONGITUDE']), float(row['LATITUDE']))


# In[ ]:





# In[6]:


schema = { 'geometry': 'Point', 'properties': {'NAME': 'str'} }
with collection(
    "some.shp", "w", "ESRI Shapefile", schema) as output:
    with open(t, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = Point(float(row['LONGITUDE']), float(row['LATITUDE']))
            output.write({
                'properties': {
                    'NAME': row['NAME']
                },
                'geometry': mapping(point)
            })


# In[7]:


with collection("some.shp", "r") as input:
    for point in input:
        print (shape(point['geometry']))


# In[8]:


with collection("some.shp", "r") as input:
    schema = { 'geometry': 'Polygon', 'properties': { 'NAME': 'str' } }
    with collection(
        "some_buffer.shp", "w", "ESRI Shapefile", schema) as output:
        for point in input:
            output.write({
                'properties': {
                    'NAME': point['properties']['NAME']
                },
                'geometry': mapping(shape(point['geometry']).buffer(0.2))
            })


# In[9]:


with collection("some_buffer.shp", "r") as input:
    schema = input.schema.copy()
    with collection(
            "some_union.shp", "w", "ESRI Shapefile", schema) as output:
        shapes = []
        for f in input:
            shapes.append(shape(f['geometry']))
        merged = cascaded_union(shapes)
        output.write({
            'properties': {
                'NAME': 'Buffer Area'
                },
            'geometry': mapping(merged)
            })


# In[ ]:





# In[ ]:




