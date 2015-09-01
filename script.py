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

	repo_count = len(list_repos)
	
	repo_info = [{'name': repo['name'], 'star_count': repo['stargazers_count']} for repo in list_repos]

	star_count = [repo['star_count'] for repo in repo_info]
	
	user_info = {'username': username,
				 'total_repos': repo_count,
				 'repo_info': repo_info,
				 'total_stars': sum(star_count)}
	return user_info
