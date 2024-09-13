import requests,sys
from config.config import config

if  config.API_TOKEN == 'YOURAPITOKEN':
    print("[Error]APITokenを指定してから実行してください。")
    sys.exit()
    

headers = {
    'Authorization': config.API_TOKEN,
    'Content-Type': 'application/json; charset=utf8',
}

url = f'{config.HOST_URL}/v1.0/devices'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    devices = response.json()  
    device_list = devices['body']['deviceList'] 
    infrared_remote_list = devices['body']['infraredRemoteList']  

    # デバイス一覧
    print("デバイス一覧:")
    for device in device_list:
        print(f"ID: {device['deviceId']}, 名前: {device['deviceName']}, タイプ: {device['deviceType']}")
        # with open('config/config.py','r') as file:
        #     lines =file.readlines()
        # with open('config/config.py','w') as file:
        #     for line in lines:
        #         if 'ContactSenser' in lines:
        #             file.write(f"    ContactSensor = '{device['deviceId']}'\n")
        #         else:
        #             file.write(line)
        # break

    # 赤外線リモート一覧
    print("\n赤外線リモート一覧:")
    for remote in infrared_remote_list:
        print(f"ID: {remote['deviceId']}, 名前: {remote['deviceName']}, タイプ: {remote['remoteType']}")
        
    

else:
    print(f'エラー: {response.status_code}')
