import requests, json


def search_endpoint_engine(api_key, title, locale):
	r = requests.get("http://api.giphy.com/v1/gifs/search?q={0}&api_key={1}&limit=1&lang={2}".format(title, api_key, locale))

	if r.status_code != 200:
		return str(r.status_code)
	else:
	    data = r.json()
	    if not data['data']:
	    	print(r.status_code)
	    	return "fail"
	    else:
		    for i in data['data']:
		    	link = i['images']['original']['url']
		    	return link


def translate_endpoint_engine(api_key, title):
	r = requests.get("http://api.giphy.com/v1/gifs/translate?s={0}&api_key={1}".format(title, api_key))

	if r.status_code != 200:
		return str(r.status_code)
	else:
	    data = r.json()
	    if not data['data']:
	    	print(r.status_code)
	    	return "fail"
	    else:
		    return data['data']['images']['original']['url']


def trending_endpoint_engine(api_key, limit):
	r = requests.get("https://api.giphy.com/v1/gifs/trending?api_key={0}&limit={1}".format(api_key, limit))

	if r.status_code != 200:
		print(r.status_code)
	else:
	    data = r.json()
	elements = []
	for i in data['data']:
	    element = {}
	    element['title'] = "Trending gif of the day"
	    element['image_url'] = i['images']['original']['url']
	    element['buttons'] = [
	        {
	            "type": "element_share"
	        }
	    ]
	    elements.append(element)
	return elements


def random_endpoint_engine(api_key, tag):
	r = requests.get("https://api.giphy.com/v1/gifs/random?api_key={0}&tag={1}".format(api_key, tag))

	if r.status_code != 200:
		print(r.status_code)
		pass
	else:
		data = r.json()

	return data['data']['image_url']