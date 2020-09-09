""" Library method to read in information from KeePass store.

This file contains functions to pull in data from KeePass using
private key based authentication.  Information stored in the database
will be used to interact with Google Domains.  The information
within the database is considered sensitive, hence the need for encryption.
"""

import os
from pykeepass import PyKeePass

KEYPASS_DB = os.environ['GOOGLE_DDNS_CLIENT_KEYPASS_DB']
KEYPASS_KEY = os.environ['GOOGLE_DDNS_CLIENT_KEYPASS_KEY']

__author__ = "Javier E. Zapanta"
__copyright__ = "Copyright 2020, Javier E. Zapanta"

__license__ = "CC BY 4.0"
__version__ = "2020.09.06.1"
__maintainer__ = "Javier E. Zapanta"
__email__ = "me@javierzapanta.com"

def get_config():
	"""This function will get the configration and return it as a dictionary.
	
	Returns
	------------------------------------------
	dict
		Dictionary containing configuration.
		TODO:  Find way to encrypt this information in memory.	
	"""

	# Load keypass database
	kp = PyKeePass(KEYPASS_DB, keyfile=KEYPASS_KEY)

	# get group entries
	group = kp.find_groups(name='db', first=True)

	# iterate through entry and build dictionary
	config = {}

	for item in group.entries:
		config[item.username] = item.password
	
	# return configuration for use
	return config