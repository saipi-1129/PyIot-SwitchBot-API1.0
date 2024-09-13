import requests,sys
from config.config import config

if not config.API_TOKEN:
    print("[Error]APIToken is empty.")
    sys.exit()
    

headers = {
    'Authorization': config.API_TOKEN,
    'Content-Type': 'application/json; charset=utf8',
}

url = f'{config.HOST_URL}/v1.0/devices'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    devices = response.json()  
    for device in devices['body']['deviceList']:
        #
        print(f"ID: {device['deviceId']}, Name: {device['deviceName']}, Type: {device['deviceType']}, Cloud: {device['enableCloudService']}, HubID: {device['hubDeviceId']}")
else:
    print(f'Error: {response.status_code}')

