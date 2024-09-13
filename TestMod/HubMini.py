import requests
from config.config import config 


def HubMini():
    url = f'{config.HOST_URL}/v1.0/devices/{config.HubMini}/status'

    response = requests.get(url, headers=config.headers)
    
    print("HubMini")

    if response.status_code == 200:
        data = response.json()
        if data['statusCode'] == 100:
            print("稼働中")
    else:
        print(f"Error{response.status_code}")