import requests
import json


def api_call(user1):
	api_url = 'https://api.github.com/users/'
	username = user1
	url = api_url + username + '/repos'
	r = requests.get(url)
	list_repos = r.json()
	
	repo_count = len(list_repos)
	total_stars = sum([repo['stargazers_count'] for repo in list_repos])
	star_list = sorted([{repo['stargazers_count']: repo['name']} for repo in list_repos], reverse=True)

	average = float(total_stars)/float(repo_count)
	
	user_info = {'username': username,
				 'total_repos': repo_count,
				 'total_stars': total_stars,
				 'sort_stars': star_list,
				 'average': average}
	return user_info
