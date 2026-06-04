import time
from selenium import webdriver
# 导入驱动对应的服务
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"D:\python\UI-automatic\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 最大化
driver.maximize_window()
# 访问商城
driver.get("https://deyunce:828123@mall.deyunce.com/")
time.sleep(1)
# 点击登录按钮
driver.find_element(By.XPATH, '//a[text()="登录"]').click()
time.sleep(1)
# 点击账号密码登录
driver.find_element(By.XPATH, '//div[contains(text(),"账号密码登录")]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//input[@placeholder="请输入账号/手机号码"]').send_keys('19903486482')
driver.find_element(By.XPATH,'//input[@placeholder="请输入密码"]').send_keys('qwezxc123')
driver.find_elements(By.XPATH,'//span[text()="立即登录"]')[1].click()
time.sleep(3)

# 关闭浏览器
driver.quit()