# -*- coding:utf-8 -*-
from selenium import webdriver
import io
import time
import json
from pprint import pprint

post = {}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
driver = webdriver.Chrome('/Users/weiweiwang/code/financialNews/chromedriver',chrome_options=chrome_options)
driver.get('https://mp.weixin.qq.com/')
time.sleep(2)
driver.find_element_by_xpath("./*//input[@name='account']").clear()
driver.find_element_by_xpath("./*//input[@name='account']").send_keys('你的账号')
driver.find_element_by_xpath("./*//input[@name='password']").clear()
driver.find_element_by_xpath("./*//input[@name='password']").send_keys('你的密码')
# 在自动输完密码之后记得点一下记住我
time.sleep(5)
driver.find_element_by_xpath("./*//a[@class='btn_login']").click()
# 拿手机扫二维码！
time.sleep(15)
driver.get('https://mp.weixin.qq.com/')
cookie_items = driver.get_cookies()
for cookie_item in cookie_items:
    post[cookie_item['name']] = cookie_item['value']
cookie_str = json.dumps(post)
with io.open('cookie.txt', 'w+') as f:
    f.write(cookie_str.decode('utf-8'))
