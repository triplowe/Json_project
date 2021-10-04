import json

infile = open("eq_data_30_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eqData = json.load(infile)

json.dump(eqData, outfile, indent=4)

print(len(eqData["features"]))

list_of_eqs = eqData["features"]
mags = []
lats = []
lons = []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    mags.append(mag)
    lat = eq["geometry"]["coordinates"][1]
    lats.append(lat)
    lon = eq["geometry"]["coordinates"][0]
    lons.append(lon)

print(mags[:5])
print(lats[:5])
print(lons[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)]

my_layout = Layout(title="Global Earthquakes 1 Day")

fig = {'data': data, 'layout' : my_layout}

offline.plot(fig, filename = "globalearthquakes1day.html")

