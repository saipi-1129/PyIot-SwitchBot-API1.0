import requests
from config.config import config 

url = f'{config.HOST_URL}/v1.0/devices/{config.WoIOSensor}/status'

def WoIOSensor():
    response = requests.get(url, headers=config.headers)

    if response.status_code == 200:
        data = response.json()  
        if data['statusCode'] == 100:
            print("稼働中:statusCode 190")
        else:
            print("稼働していません")
        print("WoIOSensor")
        print(f"温度:{data['body']['temperature']}\n湿度:{data['body']['humidity']}\n")
    else:
        print(f"Error {response.status_code}")
