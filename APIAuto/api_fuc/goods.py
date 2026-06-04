import requests
from common.address import url_search
from common.public_vars import headers
from common.public_func import get_token
def search_goods(goods_name, page_size=20):
    uploads = {
        "page_size": page_size,
        "name": goods_name
    }
    # 给头信息添加token
    headers["token"] =get_token()

    response = requests.get(url=url_search, params=uploads, headers=headers)
    return response

# search_goods("手机")