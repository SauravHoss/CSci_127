#Saurav Hossain
#09/21/18
#Collision Maps

import folium
import pandas as pd

x = input()
y = input()

cm = pd.read_csv(x)

acm = folium.Map(location=[40.768731, -73.964915])
for index,row in cm.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    newMarker = folium.Marker([lat, lon])
    newMarker.add_to(acm)
acm.save(outfile = y)
