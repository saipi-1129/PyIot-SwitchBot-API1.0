import requests
from config.config import config 


def PlugMini():
    url = f'{config.HOST_URL}/v1.0/devices/{config.PlugMini}/status'

    response = requests.get(url, headers=config.headers)
    print("PlugMini")

    if response.status_code == 200:
        data = response.json()
        if data['statusCode'] == 100:
            print("稼働中")
        else:
            print("Error")
        print(f"電源: {data['body']['power']}")
        print(f"電圧: {data['body']['voltage']}V")
        print(f"重量: {data['body']['weight']}kg")
        print(f"今日の電力消費: {data['body']['electricityOfDay']}Wh")
        print(f"電流: {data['body']['electricCurrent']}A")
    else:
        print(f"Error{response.status_code}")