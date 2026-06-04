from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.loginout_page import Loginout_Page


class TestLogin:  # 测试登录类
    def test_login_success(self):
        # 先打开首页，点击登录，输入账号密码，点击登录，断言登录成功

        # 首页的操作==============================
        hp = HomePage()
        hp.open_mall()  # 打开商城
        hp.goto_login_page()  # 点击登录，跳转到登录页面

        # 登录页操作=================
        lp = LoginPage()
        lp.login()  # 调用登录的方法

        lpt=Loginout_Page()
        lpt.loginout()

