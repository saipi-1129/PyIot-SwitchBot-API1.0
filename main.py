from concurrent.futures import ThreadPoolExecutor
from TestMod.ContactSensor import ContactSensor
from TestMod.WoIOSensor import WoIOSensor
from TestMod.HubMini import HubMini 
from TestMod.PlugMini import PlugMini

def initialize_contact_sensor():
    return ContactSensor()

def initialize_woio_sensor():
    return WoIOSensor()

def initialize_hub_mini():
    return HubMini()

def initialize_plug_mini():
    return PlugMini()

with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(initialize_contact_sensor),
        executor.submit(initialize_woio_sensor),
        executor.submit(initialize_hub_mini),
        executor.submit(initialize_plug_mini)
    ]


print("\nタスク終了。何かキーを押してください。")
input()