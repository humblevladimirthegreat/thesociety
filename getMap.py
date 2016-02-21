import urllib

'''
import json

query = '' # IP to get coordinates of, leave empty for current IP

geo = urllib.urlopen('http://ip-api.com/json/%s?fields=240' % query)
print geo
help(geo)
result = json.load(geo)
if result['zip']:
    zoom = 13
elif result['city']:
    zoom = 12
else:
    zoom = 6
map_img_url = "https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zoom=%i&size=320x385&sensor=false" % (result['lat'], result['lon'], zoom)
get_map_img = urllib.urlretrieve(map_img_url, "staticmap.png")
'''
def save_map(lat, lon, filename='map.png', zoom=6):
	map_img_url = "https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zoom=%i&size=320x385&sensor=false" % (lat, lon, zoom)
	urllib.urlretrieve(map_img_url, filename)
