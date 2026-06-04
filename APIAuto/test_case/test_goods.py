from api_fuc.goods import search_goods

def test_search_goods():
    res=search_goods('德云测')
    assert res.status_code==200
    goods_list=res.json()['data']['list']
    goods_1=goods_list[0]
    assert '德云测' in goods_1['name']