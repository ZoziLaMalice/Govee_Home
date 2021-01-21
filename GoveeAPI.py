import requests

def get_info():
    headers = {"Govee-API-Key": "cbdd1086-bd4b-47c2-9b47-39717902f2ed"}
    r = requests.get('https://developer-api.govee.com/v1/devices',
                    headers=headers)
    print(r.text)
    return r

def cmd(name, value):
    headers = {"Govee-API-Key": "cbdd1086-bd4b-47c2-9b47-39717902f2ed",
            "Content-Type": "application/json"}
    params = {"device": "BD:B7:A4:C1:38:E6:78:B2",
            "model": "H6159",
            "cmd": {
                "name": name,
                "value": value
            }}
    r = requests.put('https://developer-api.govee.com/v1/devices/control', json=params, headers=headers)
    print(r.text)
    return r

def get_state():
    headers = {"Govee-API-Key": "cbdd1086-bd4b-47c2-9b47-39717902f2ed",
            "Content-Type": "application/json"}
    params = {"device": "BD:B7:A4:C1:38:E6:78:B2",
            "model": "H6159"}
    r = requests.get('https://developer-api.govee.com/v1/devices/state?',
                    params=params, headers=headers)
    print(r.text)
    return r



