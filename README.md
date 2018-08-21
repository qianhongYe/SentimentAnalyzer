# WikiSentiViewer

A widget to show sentiment distribution on geolocation for Wikipedia entities (concepts).

Wikipedia entities contains entities in Wikipedia Article and Wikipedia Talk. Talk page is an area for editors to discuss about corresponding article, which can be visited from upper left side of article page.

This widget includes entities having geolocation information. 

The text of Articles and Talks is extracted from Wikipedia Dump. The geolocation and time stamps are extracted from DBPedia. The date for people indicates birth date, while the date for events indicates occurrance date.

The scores are calculated with term frequency for sentiment words based on certain lexicons (OL, MPQA, LIWC, ANEW). For ANEW we take valency into account too.

## How to use it

1. You can use the link below to run this jupyter notebook with mybinder.

https://mybinder.org/v2/gh/qianhongYe/WikiSentiViewer/master

It takes around 10 mins to prepare the environment.

2. Click geomap.ipynb in the home page to open the notebook.

3. You can open Appmode to ignore the codes by clicking "Appmode" in toolbar (recommended for general user). Alternatively, you can choose "Run All" inside Cell menu without entering appmode (recommended for programmer).

Now you can operate with the widget.

## What can be seen with the widget

After selecting value for required field and click "Go" button, it comes up with plot.

For each run you will see a new map with circles on it. Each circle represents an entity.

The size of the circle indicates the total score of its sentiment, the color indicates the balance of positive/negative sentiment, in which red represents negative whereas blue represents positive.

In the bottom you will get the data characteristics for the current run.

## Run it locally

If you want to run it locally, you need to install libraries listed in environment.yml with version showed in requirements.txt. Dataset can download dataset in the following link.

https://www.dropbox.com/sh/mt7by5f1wgl6n3z/AACddwkFPq5lPpH3ry83MgSDa?dl=0
