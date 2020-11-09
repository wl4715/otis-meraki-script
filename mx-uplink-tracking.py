"""

	This code requires completion: 
		after we change uplink to WAN 2 
		we need to also monitor the behavior of WAN 2
		and switch back to WAN 1, etc.


"""

### ------------------------LIBRARIES-----------------------------------
import json
import requests

### ------------------------CREDENTIALS-----------------------------------
# retrieve credentials from env_user.py file
from env_user import 
	api_key, 
	dashboard_url, 
	network_id,
	serial

# define the header Meraki API Key used in all functions
headers = {
	'X-Cisco-Meraki-API-Key' : api_key
}

### ------------------------FUNCTIONS-----------------------------------
# this function retrieves the loss and latency of the MX uplink WAN 1 
def get_uplink_loss_and_latency(serial):
	payload = {
		'ip' : '8.8.8.8',
		'uplink' : wan1,
		'timespan' : 180
	}

	response = requests.get(
					dashboard_url + '/devices/' + serial + '/lossAndLatencyHistory',
					headers = headers,
					params = payload
				).json()


	loss = response[0]['lossPercent']
	latency = response[0]['latencyMs']

	return loss, latency

# this function changes the preferred MX uplink to WAN 2
def change_default_uplink(network_id):
	payload = {
		"defaultUplink" : wan2 
	}

	response = requests.put(
					dashboard_url + '/networks/' + network_id + '/appliance/trafficShaping/uplinkSelection',
					headers = headers,
					data = payload
				)

### --------------------------MAIN--------------------------------------
if __name__ == '__main__':

	# In production, this should be running in a while loop

	loss, latency = get_uplink_loss_and_latency(serial)
	print('loss of WAN 1: ', loss, '%')
	print('latency of WAN 2: ', latency, 'ms')

	# Change the threshold parameters, currently at 50% loss and 150 ms latency
	if (loss > 0.5) or (latency > 150):
		change_default_uplink(network_id)

