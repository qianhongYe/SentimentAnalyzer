# SentimentAnalyzer
A framework to visualize the sentiment distribution of wikipedia articles.

Open geomap.ipynb with Jupyter Notebook to run this framework.

Notes:

1. Use command as below in terminal to open notebook, in order to avoid out of io_limit.
jupyter notebook --NotebookApp.iopub_data_rate_limit=2147483647

2. Involved library

Here are some involved libraries...
**********************
matplotlib
shapely.geometry
pandas
geopandas
ipywidgets
Ipython.display
folium
datetime
dateutil
traitlets
json
**********************

You might need to install some of them if you meet any error like "There is no module ..." while you do the following import. These import are in the front of geomap.ipynb
**********************
import matplotlib as mpl
import matplotlib.pyplot as plt
from shapely.geometry import Point
import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame
from ipywidgets import widgets 
from ipywidgets import *  
from IPython.display import display,clear_output
from ipywidgets import Layout
import folium
from datetime import datetime
from datetime import date
from dateutil import rrule
from traitlets import directional_link
import json
**********************


3. Put the following folder or files to current directory, which you could find in Amazon Driver ...
**********************
score_file
docs_length.csv
person_birthdate.json
event_date.json
title_geo_country_continent.csv
eventList.json
PersonList.json
**********************








