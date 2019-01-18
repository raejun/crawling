# conda install selenium
from selenium import webdriver
import time

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(5)

assert "Google" in driver.title

# <input name="q" ... >
elem = driver.find_element_by_name("q")
elem.clear()  # 혹시 내용이 있으면 지운다.
elem.send_keys("미세먼지")  # 입력
elem.submit()

time.sleep(30)
driver.close()
