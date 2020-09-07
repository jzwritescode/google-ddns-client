import requests
from requests.auth import HTTPBasicAuth
import backoff
from base64 import b64encode


def unable_to_get_url(ex):
	"""Exception handing routine if unable to get IP address
	
	Parameters
	----------
	ex:		object
		Exception object.  Currently using base RequestException 
		from requests.
	
	"""

	print("Issue calling Google API")
	print(ex)
	exit(2)

@backoff.on_exception(backoff.expo,
                      requests.exceptions.RequestException,
                      max_time=30,
                      giveup=unable_to_get_url)
def set_ip_address(config: dict, ip_info: dict) -> dict:
	"""Update Google DNS entry with IP address.
	
	Parameters
	----------
	config:		dict
		Dictionary containing 
	ip_info:	dict
		Dictionary containing IP information.

	Returns
	-------
	dict
		Response from POST request.
	
	"""

	url = "https://domains.google.com/nic/update?hostname={0}&myip={1}"

	response = requests.post(url.format(config['hostname'], ip_info['ip']),auth=HTTPBasicAuth(config['username'], config['password']))
	print(response)



