# otis-meraki-script
This script shows how we can track the latency and loss of MX uplink WAN 1 and switch to WAN 2 if a threshold is met.

Set up steps:

	1) Change the credentials in env_user.py

	2) Set up the environment:
		% python3 -m venv venv
		% source venv/bin/activate
		% pip install -r requirements.txt

	3)Run this code:
		% python3 mx-uplink-tracking.py
