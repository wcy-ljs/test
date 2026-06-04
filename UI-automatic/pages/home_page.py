import time

from pages.base_page import BasePage


class HomePage(BasePage):
    url = "https://deyunce:828123@mall.deyunce.com/"
    loc_login = '//a[text()="登录"]'

    def open_mall(self):  # 打开商城
        self.open_url(self.url)
        time.sleep(1)

    def goto_login_page(self):  # 点击登录，进入登录页面
        self.click(self.loc_login)
        time.sleep(1)


