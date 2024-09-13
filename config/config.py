
class config:
    # SwitchBot APIのトークンを設定(スマホアプリから確認)
    API_TOKEN = 'YOURAPITOKEN'
    
    HOST_URL = "https://api.switch-bot.com"
    
    headers = {
    'Authorization': API_TOKEN,
    'Content-Type': 'application/json; charset=utf8',}
    
    # デバイスIDを設定(list.pyを実行し任意のIDを入力)
    ContactSensor= 'DEVICEID'
    
    WoIOSensor ="DEVICEID"
    
    HubMini= "DEVICEID"
    
    PlugMini ="DEVICEID"