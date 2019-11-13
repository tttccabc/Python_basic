# -- coding:utf-8 --
# https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6
from selenium import webdriver
import os

chromedriver = 'D:\Project&Files\chromedriver\chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
url = 'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6'
driver.get(url)

driver.implicitly_wait(5)  # 加载完成则完成，最长5秒
# 需要加延迟，因为页面加载需要时间
data = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[2]/span[1]/a').get_attribute('href')
