from pages.base_page import BasePage
import time

class Loginout_Page(BasePage):
    loc_out_login = '//a[@href="/pc/user/profile"]'
    loc_out_login_btn = '//div[contains(text(),"退出登录")]'

    def loginout(self):
        self.click_1(self.loc_out_login, 0)
        self.click(self.loc_out_login_btn)