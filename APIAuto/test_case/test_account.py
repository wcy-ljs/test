from api_fuc.account import login
def test_login():
    res=login("19903486482")
    status_code=res.status_code
    assert status_code==200

    res_json=res.json()
    print(res_json)

    msg =res.json()['msg']
    nickname=res.json()['data']['nickname']
    assert msg=='登录成功'
    assert nickname=='19999999999'