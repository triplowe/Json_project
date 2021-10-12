from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('US_fires_9_14.json', 'r')

fires = json.load(infile)

#print(len(fires))
#print(type(fires))

lats, lons, brights = [], [], []

for fire in fires:
    bright = fire['brightness']
    if bright > 450:
        lat = fire['latitude']
        lon = fire['longitude']
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

#print(lats[:5])
#print(lons[:5])
#print(brights[:5])
#print(len(brights))

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*3 for b in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    }
}]

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='US_Fires_9_14.html')