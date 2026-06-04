import requests
from common.address import url_login
from common.public_vars import headers

def login(account,password='qwezxc123',client=5):
    uploads = {
        "account": account,
        "password": password,
        "client": client
    }
    response=requests.post(url=url_login,headers=headers,json=uploads)
    return response

# login("19903486482")