import requests
import json
#from requests.exceptions import RequestException
#from contextlib import closing
from bs4 import BeautifulSoup

def get_url(url):
	"""
	Returns the HTML/XML content of the URL by making a GET request
	"""

	r = requests.get(url)

	return r.text

def ad(html):
	"""
	returns each add
	"""

	soup = BeautifulSoup(html, 'html.parser')

	"""
	soup.find_all("div", {'class': lambda x: x 
                       and 'search-item' in x.split()
             })
	"""

	return soup.select('.search-item')

def price(soup):
	"""
	returns the price of an listing
	"""

	soup.select('.price')

	return soup.text

def title(soup):
	"""
	returns the title of a listing
	"""

	soup.select(".price")

	return soup.text