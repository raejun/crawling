# conda install selenium
from selenium import webdriver
import time

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get("https://www.google.com/")
time.sleep(5)
driver.close()
