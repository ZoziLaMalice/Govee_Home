import requests

headers = {"Govee-API-Key": "cbdd1086-bd4b-47c2-9b47-39717902f2ed"}
r = requests.get('https://developer-api.govee.com/v1/devices', headers=headers)
print(r.text)

headers = {"Govee-API-Key": "cbdd1086-bd4b-47c2-9b47-39717902f2ed",
           "Content-Type": "application/json"}
r = requests.get('https://developer-api.govee.com/v1/devices/control', headers=headers)
print(r.text)
