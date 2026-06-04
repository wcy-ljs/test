from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    loc_acc_pwd = '//div[contains(text(),"账号密码登录")]'
    loc_acc = '//input[@placeholder="请输入账号/手机号码"]'
    loc_pwd = '//input[@placeholder="请输入密码"]'
    loc_login_btn = '//span[text()="立即登录"]'

    account = "19903486482"
    password = "qwezxc123"

    def login(self):
        self.click(self.loc_acc_pwd)  # 点击账号密码登录
        self.send(self.loc_acc, self.account)  # 输入账号
        self.send(self.loc_pwd, self.password)  # 输入密码
        self.click_1(self.loc_login_btn, 1)  # 点击立即登录


