from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import calendar
from selenium import webdriver

main_url = "http://192.168.50.224"
driver = webdriver.Chrome("C:/driver/chromedriver.exe")
a=0
while a < 5000:
    a += 1
    driver.get(main_url)