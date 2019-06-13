from requests import HTTPSession
#from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def get_url(url):
	"""
	Returns the HTML/XML content of the URL by making a GET request
	"""
	http = HTTPSession()

	r = http.request('get', url)

	return r

