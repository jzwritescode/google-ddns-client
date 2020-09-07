""" Get current ISP IP address.

This file contains functions to support the retrieval of an IPv4/6 IP address.
"""


import requests
import backoff

__author__ = "Javier E. Zapanta"
__copyright__ = "Copyright 2020, Javier E. Zapanta"

__license__ = "CC BY 4.0"
__version__ = "2020.09.06.1"
__maintainer__ = "Javier E. Zapanta"
__email__ = "me@javierzapanta.com"

def unable_to_get_url(ex):
	"""Exception handing routine if unable to get IP address
	
	Parameters
	----------
	ex:		object
		Exception object.  Currently using base RequestException 
		from requests.
	
	"""

	print("Issue getting URL")
	print(ex)
	exit(1)

@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_time=30,
                      giveup=unable_to_get_url)
def request_ip(url) -> str:
	"""Returns IP address based on URL.

	Parameters
	----------
	url:	str
		URL to query

	Returns
	-------
	str
		IP address
	
	"""

	r = requests.get(url)
	return r


def get_ip_v4_address() -> dict:
	""" Returns IP address of client ISP as dictionary.  Using Google's IP Address utility.

	Arguments
	---------

	ipv4:	bool
		Query for IPv4 address?
	ipv6:	bool
		Query for IPv6 address?

	Returns
	-------
	dict
		A list containing a combination of IPv4, IPv6, or both IPv4/6 addresses

	"""
	
	url = "https://domains.google.com/checkip"
	response = request_ip(url)
	ip = {}
	ip['ip'] = response.text
	ip['status_code'] = response.status_code

	return ip