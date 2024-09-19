from config.config import config
import requests 

print('setup.batを実行し、電源をつけるデバイスのIDを張り付けてください。')
deviceid = input("Id:")

url = f'https://api.switch-bot.com/v1.0/devices/{deviceid}/commands'

data = {
    'command': 'turnOn',
    'parameter': 'default',
    'commandType': 'command'
}

response = requests.post(url, json=data, headers=config.headers)

if response.status_code == 200:
    print(f'[{response.status_code}]Id:{deviceid}の電源をつけました。')
else:
    print(f'エラー: {response.status_code}, {response.text}')
