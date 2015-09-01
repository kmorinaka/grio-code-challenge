import requests
import urllib2
import urllib
import json
from pprint import pprint

URL = 'https://api.github.com/users'


def api_call(user1):
	api_url = 'https://api.github.com/users/'
	username = user1
	url = api_url + username + '/repos'
	r = requests.get(url)
	list_repos = r.json()

	return list_repos
