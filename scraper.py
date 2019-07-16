import requests
import json
import re
#from requests.exceptions import RequestException
#from contextlib import closing
from bs4 import BeautifulSoup

def get_url(url):
	"""
	Returns the HTML/XML content of the URL by making a GET request
	"""

	r = requests.get(url)

	return r.content

def ad(html):
	"""
	returns each add
	"""

	soup = BeautifulSoup(html, 'html.parser')

	return soup.select('.search-item')

def price(soup):
	"""
	takes a single ad (html glob)
	returns the price of an listing
	"""
	# could make this more efficent but eh
	data_list = [element.text for element in soup.find_all("div", "price")]

	tag_price = re.compile('[0-9.,]')
	
	return ''.join(tag_price.findall(data_list[0]))

def title(soup):
	"""
	returns the title of a listing
	"""

	data_list = [element.text for element in soup.find_all("div", "title")]

	return data_list[0].strip()

def description(soup):
	"""
	takes a singe ad
	returns the description of the ad
	"""

	data_list = [element.text for element in soup.find_all("div", "description")]

	return data_list[0].strip()

def location(soup):
	"""
	takes a singe ad
	returns the location of the ad
	"""

	data_list = [element.text for element in soup.find_all("div", "location")]

	return data_list[0].strip()


def kilometers(soup):
	"""
	takes a singe ad
	returns the kilometers of the ad
	"""

	data_list = [element.text for element in soup.find_all("div", "details")]

	return data_list[0].strip()

def link(soup):
	"""
	takes a single ad
	returns the link of the ad
	"""

	data_list = [element.text for element in soup.find_all("a", "title")]


	return data_list[0]