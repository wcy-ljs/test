import requests
from common.address import url_login
from common.public_vars import headers

def get_token(account='19903486482',password='qwezxc123',client=5):
    uploads = {
        "account": account,
        "password": password,
        "client": client
    }
    response = requests.post(url=url_login, headers=headers, json=uploads)
    rse_json=response.json()
    return rse_json['data']['token']