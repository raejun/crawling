import math
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
from selenium.webdriver.chrome.options import Options

main_url = "https://www.skyscanner.co.kr/"
keyword = "오사카"

options = Options()
options.add_argument('--no-sandbox') # Bypass OS security model
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
driver.get(main_url)
driver.implicitly_wait(10)

# 편도 클릭

one_way = driver.find_element_by_id("fsc-trip-type-selector-one-way")
one_way.click()
time.sleep(3)

destination = driver.find_element_by_css_selector("#destination-fsc-search")
destination.clear()

destination.send_keys(keyword)


time.sleep(3)
start_day = driver.find_element_by_css_selector("#depart-fsc-datepicker-button")
start_day.click()


# 출발 날짜 클릭
time.sleep(3)
start = driver.find_element_by_css_selector("#depart-fsc-datepicker-button")
start.click()

#달력에서 동그라미쳐진 날짜 클릭
time.sleep(3)
start_day = driver.find_element_by_css_selector("#depart-fsc-datepicker-popover > div > div > div.fsc-datepicker__container-3azq_ > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > button")
start_day.click()
# '직항만' 체크
time.sleep(3)
check_non_stop = driver.find_element_by_css_selector("div.SingleDestControls-2wsUo > label > input")
check_non_stop.click()

# 항공권 검색 클릭
time.sleep(2)
search = driver.find_element_by_css_selector("#flights-search-controls-root > div > div > form > div:nth-child(3) > button")
search.click()