"""
	Go to Organization > Settings and tick on API Access
	Then head to your Profile, where you will find your API Key

"""
# replace your API key here
api_key = "abcdefgh123456789" 



"""
	Go to your Meraki Dashboard
	Find the n255, n143, etc. that corresponds to your dashboard organization

"""
# replace 'xxx' by the your dashboard number
dashboard_url = "https://nxxx.meraki.com/api/v1" 



"""
	To find your network_id:
		1) Find your Organization_id 
			https://developer.cisco.com/meraki/api-v1/#!get-organizations
		2) Use the Organization_id and find your network_id 
			https://developer.cisco.com/meraki/api-v1/#!get-organization-networks 

"""
# replace your network id here
network_id = "L_12334566789"



"""
	To find your the serial number of the MX:
		1) Find it in Dashboard 
		2) Use the network_id and list all devicees 
			https://developer.cisco.com/meraki/api-v1/#!get-network-devices

"""
# replace your MX serial here
network_id = "Q1C1-A2B2-C3D3"
