import urllib, urllib2
import config
import utils
import json

try:
	import xbmc, xbmcgui, xbmcplugin
except ImportError:
	pass # for PC debugging

cache = False

def fetch_url(url, token=None):
	"""
		Simple function that fetches a URL using urllib2.
		An exception is raised if an error (e.g. 404) occurs.
	"""
	utils.log("Fetching URL: %s" % url)

	# Token headers
	headers = {}
	if token:
		headers = {'x-media-mis-token': token} 

	request = urllib2.Request(url, headers=headers)
	return urllib2.urlopen(request).read()


def fetch_token():
	"""
		This functions performs a HTTP POST to the token URL
		and it will return a token required for API calls
	"""	
	req = urllib2.Request(config.TOKEN_URL, '')
	res = urllib2.urlopen(req)
	json_result = json.loads(res.read())
	res.close()
		
	return json_result['token']


def get_stations():

	# Get a token. TODO: Cache this
	token = fetch_token()

	data = fetch_url(config.LIVE_AUDIO_URL, token)

	json_data = json.loads(data)

	station_list = json_data['matchAudioStreams']

	if len(station_list) == 0:
		return None

	return station_list[0]['audioStreams']

