""" Main program for getting updated IP address using 3rd party library

This file contains the code to run through the process of getting an IP address.
Use of exponential backoff will be used.  If the program fails to obtain an IP
address, then it will return an appropriate error message.
"""

import config_keypass as kp
import google_ddns as google
import get_ip as ip

def main():
	"""Main function."""
	ipv4 = ip.get_ip_v4_address()
	config = kp.get_config()
	google.set_ip_address(config, ipv4)

# Call main function.
main()