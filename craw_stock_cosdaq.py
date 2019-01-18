import time
import math
# import pymysql
from bs4 import BeautifulSoup
import datetime
import pandas as pd

from selenium import webdriver


# # https://selenium-python.readthedocs.io/waits.html#explicit-waits 코드를 복사
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options



main_url = "http://marketdata.krx.co.kr/mdi#document=040602"
driver = webdriver.Chrome("C:/driver/chromedriver.exe")

# # options = Options()
# # options.add_argument('--no-sandbox') # Bypass OS security model
# # driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
# driver.get(main_url)
# time.sleep(3) # 무조건 정해진 시간(초) 쉰다.
 

# # Auction_list = []
# # def insert_auction(auction):
# #     conn = pymysql.connect(host='localhost', user='root', password='qkr402', db='auction', charset='utf8')
# #     cur = conn.cursor()
# #     sql = """INSERT INTO apart_auction(str_link, str_land_num, str_land_type, str_land_area, str_land_high_price, str_land_low_price, str_land_condition, str_land_date, str_land_count, str_land_surface, str_land_site, str_land_disposal_date, str_land_floor, str_land_room_structure, str_land_feature) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# #     cur.execute( sql, auction )
# #     conn.commit()
# #     conn.close()
# #     print("저장 성공!")
 

# df_hdays2015 = pd.read_excel('http://bitly.kr/m5PD')
# df_hdays2016 = pd.read_excel('http://bitly.kr/Jo6p')
# df_hdays2017 = pd.read_excel('http://bitly.kr/ztxA')
# #df_hdays2018 = pd.read_excel('http://bitly.kr/zBpM')
 

# hdays2015 = df_hdays2015['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
# hdays2015 = pd.to_datetime(hdays2015)
# hdays2015.name = '2015'
 

# hdays2016 = df_hdays2016['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
# hdays2016 = pd.to_datetime(hdays2016)
# hdays2016.name = '2016'
 

# hdays2017 = df_hdays2017['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
# hdays2017 = pd.to_datetime(hdays2017)
# hdays2017.name = '2017'
 

# hdays2018 = df_hdays2018['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
# hdays2018 = pd.to_datetime(hdays2018)
# hdays2018.name = '2018'
 

# stock_days = pd.date_range('20150101', '20181128', freq='B')
# stock_days = stock_days.drop(hdays2015)
# stock_days = stock_days.drop(hdays2016)
# stock_days = stock_days.drop(hdays2017)
# stock_days = stock_days.drop(hdays2018)
 

# stockdays_list = stock_days.strftime("%Y%m%d").tolist()
# print(stockdays_list)
 

# t = 0
# try:
#     for stock_3years in stockdays_list:
#         kosdaq_click = driver.find_element_by_id("market_gubun2a87ff679a2f3e71d9181a67b7542122c").click()
#         print("여기까지됨")
#         time.sleep(3)
#         day_search = driver.find_element_by_id("schdated3d9446802a44259755d38e6d163e820")
#         day_search.clear()
#         day_search.send_keys(stock_3years)
#         print("여기까지됨")
#         t += 1
#         time.sleep(1)
#         search = driver.find_element_by_id("btnidc81e728d9d4c2f636f067f89cc14862c").click()
#         # stockdata_down = driver
 

# except Exception as e1 :
#     print("e1=============", e1)
# finally:
#     driver.close()
