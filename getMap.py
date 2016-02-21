import urllib
import Image


def save_map(lat, lon, filename='map.png', zoom=20, show=True):
	map_img_url = "https://maps.googleapis.com/maps/api/staticmap?center=%s,%s&zoom=%i&size=320x385&sensor=false" % (lat, lon, zoom)
	urllib.urlr]etrieve(map_img_url, filename)
		
if __name__ == '__main__':  #sample script that gets map of location at current IP address
	import json
	query = '' # IP to get coordinates of, leave empty for current IP
	geo = urllib.urlopen('http://ip-api.com/json/%s?fields=240' % query)
	result = json.load(geo)
	save_map(result['lat'], result['lon'])
	image = Image.open(filename)
	image.show()
