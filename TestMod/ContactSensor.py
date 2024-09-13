import requests,sys
from config.config import config 

def ContactSensor():
    url = f'{config.HOST_URL}/v1.0/devices/{config.ContactSensor}/status'

    response = requests.get(url, headers=config.headers)
    
    print("ContactSensor")

    if response.status_code == 200:
        data = response.json()
        if data['statusCode'] == 100:
            print("稼働中:statusCode 190")
        else:
            print("稼働していません")
            
        if data['body']['openState'] == 'open':
            print('ドアが開いています')
        else:
            print('ドアが閉まっています')
            
        if data['body']['moveDetected'] == True:
            print("動体を検知しました")
        else:
            print("動体は検知されませんでした")
            
    else:
        print(f'エラー: {response.status_code}')

