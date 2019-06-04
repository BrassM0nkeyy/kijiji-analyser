from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def get_url(url):
	"""
	Returns the HTML/XML content of the URL by making a GET request
	"""
	try:
		resp = get(url, stream=True)
		return resp.content

	except RequestException as e:
		log_error('it didnt work {0}'.format(str(e)))
		return None