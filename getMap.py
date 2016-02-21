import urllib.request

def save_map(lat, lon, filename='map.png', zoom=20, show=True):
    map_img_url='https://maps.googleapis.com/maps/api/staticmap' + \
                '?center=' + str(lat) + ',' + str(lon) + '&zoom=' + str(zoom) + \
                '&size=800x800&maptype=satellite' + \
                '&key=AIzaSyCkZrerI4yupJXV93iAPkTnpbgMVpiHdj0'
    urllib.request.urlretrieve(map_img_url, filename)

if __name__ == '__main__':  #sample script that gets map of location at current IP address
	import json
	query = '' # IP to get coordinates of, leave empty for current IP
	response = urllib.request.urlopen('http://ip-api.com/json/%s?fields=240' % query)
	geo = response.read().decode()
	result = json.loads(geo)
	save_map(result['lat'], result['lon'])
