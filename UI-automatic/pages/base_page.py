import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class BasePage:
    driver = None

    # 构造方法,打开浏览器，实现浏览器只打开一次
    def __init__(self):
        if BasePage.driver == None:
            service = Service(executable_path=r"D:\python\UI-automatic\drivers\chromedriver.exe")
            BasePage.driver = webdriver.Chrome(service=service)

            # 最大化
            BasePage.driver.maximize_window()
    def open_url(self, url):  # 打开网站
        self.driver.get(url)
    # def find(self,by,locator):  # 查找元素  by 定位方式  locator 元素定位表达式

    def find(self, locator):  # 查找单个元素  locator: xpath元素定位表达式
        ele = self.driver.find_element(By.XPATH, locator)
        return ele

    def finds(self, locator):  # 查找多个元素  locator: xpath元素定位表达式
        ele = self.driver.find_elements(By.XPATH, locator)
        return ele

    def click(self, locator):  # 点击单个元素
        self.find(locator).click()

    def send(self,locator,text):
        self.find(locator).send_keys(text)

    def click_1(self, locator,index):  # 点击多个元素中的一个
        self.finds(locator)[index].click()

    def send_1(self, locator, index, text):  # 往多个元素中的某一个  输入内容
        self.finds(locator)[index].send_keys(text)




BasePage()

