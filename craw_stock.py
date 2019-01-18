import time
import math
import pymysql
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import codecs
import os
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import calendar
from selenium import webdriver


# # https://selenium-python.readthedocs.io/waits.html#explicit-waits 코드를 복사
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options



main_url = "http://marketdata.krx.co.kr/mdi#document=040602"
driver = webdriver.Chrome("C:/driver/chromedriver.exe")

# options = Options()
# options.add_argument('--no-sandbox') # Bypass OS security model
# driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
driver.get(main_url)
time.sleep(3) # 무조건 정해진 시간(초) 쉰다.
 
# DB 테이블에 넣을 함수 만들기
def insert_data(cos):
    conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='stock', charset="utf8")
    cur = conn.cursor()
    sql = """ INSERT INTO stock(code,name,npr,op,creper,msh,mbh,tr_ct,tr_pr,tpr,hpr,lpr,acpr,money,tcoun,totpr,what,date)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(sql, cos)
    conn.commit()
    conn.close()

# 증시 휴장일 excel 파일 가져오기
df_hdays2009 = pd.read_excel('http://bitly.kr/4wuD')
df_hdays2010 = pd.read_excel('http://bitly.kr/LIo9')
df_hdays2011 = pd.read_excel('http://bitly.kr/uY2r')
df_hdays2012 = pd.read_excel('http://bitly.kr/H8Ub')
df_hdays2013 = pd.read_excel('http://bitly.kr/wgon')
df_hdays2014 = pd.read_excel('http://bitly.kr/x4cY')
df_hdays2015 = pd.read_excel('http://bitly.kr/m5PD')
df_hdays2016 = pd.read_excel('http://bitly.kr/Jo6p')
df_hdays2017 = pd.read_excel('http://bitly.kr/ztxA')
df_hdays2018 = pd.read_excel('http://bitly.kr/zBpM')
 
# 증시휴장일 EXCEL 파일에서 날짜 추출
hdays2009 = df_hdays2009['일자 및 요일']
hdays2009 = pd.to_datetime(hdays2009)
hdays2009.name = '2009'

hdays2010 = df_hdays2010['일자 및 요일']
hdays2010 = pd.to_datetime(hdays2010)
hdays2010.name = '2010'

hdays2011 = df_hdays2011['일자 및 요일']
hdays2011 = pd.to_datetime(hdays2011)
hdays2011.name = '2011'

hdays2012 = df_hdays2012['일자 및 요일']
hdays2012 = pd.to_datetime(hdays2012)
hdays2012.name = '2012'

hdays2013 = df_hdays2013['일자 및 요일']
hdays2013 = pd.to_datetime(hdays2013)
hdays2013.name = '2013'

hdays2014 = df_hdays2014['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
hdays2014 = pd.to_datetime(hdays2014)
hdays2014.name = '2014'

hdays2015 = df_hdays2015['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
hdays2015 = pd.to_datetime(hdays2015)
hdays2015.name = '2015'
 

hdays2016 = df_hdays2016['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
hdays2016 = pd.to_datetime(hdays2016)
hdays2016.name = '2016'
 

hdays2017 = df_hdays2017['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
hdays2017 = pd.to_datetime(hdays2017)
hdays2017.name = '2017'
 

hdays2018 = df_hdays2018['일자 및 요일'].str.extract('(\d{4}-\d{2}-\d{2})', expand=False)
hdays2018 = pd.to_datetime(hdays2018)
hdays2018.name = '2018'
 
# EXCEL에서 가져온 휴장일 날짜를 전체 날짜에서 드롭
stock_days = pd.date_range('20010120', '20181128', freq='B')
stock_days = stock_days.drop(hdays2009)
stock_days = stock_days.drop(hdays2010)
stock_days = stock_days.drop(hdays2011)
stock_days = stock_days.drop(hdays2012)
stock_days = stock_days.drop(hdays2013)
stock_days = stock_days.drop(hdays2014)
stock_days = stock_days.drop(hdays2015)
stock_days = stock_days.drop(hdays2016)
stock_days = stock_days.drop(hdays2017)
stock_days = stock_days.drop(hdays2018)
 

stockdays_list = stock_days.strftime("%Y%m%d").tolist()
print(stockdays_list)
 


try:
    for stock in stockdays_list:
        # kosdaq_click = driver.find_element_by_id("market_gubun2a87ff679a2f3e71d9181a67b7542122c").click()
        print("여기까지됨")
        time.sleep(3)
        day_search = driver.find_element_by_id("schdated3d9446802a44259755d38e6d163e820")
        day_search.clear()
        day_search.send_keys(stock)
        print("여기까지됨")
        
        search = driver.find_element_by_id("btnidc81e728d9d4c2f636f067f89cc14862c").click()
        time.sleep(2)
        # stockdata_down = driver
        driver.find_element_by_xpath("//*[@id='6512bd43d9caa6e02c990b0a82652dca']/button[3]").click()
        time.sleep(2)
        f = codecs.open("C:/Users/Playdata/Downloads/data.csv", 'r', 'utf-8')
        li1 = []
        rdr = csv.reader(f)
        print(rdr)
        for line in rdr:
            if line[1] == "종목명":
                continue
            line.append(stock)
            li1.append(line)
        f.close()
        os.remove("C:/Users/Playdata/Downloads/data.csv")
        for cos in li1:
            insert_data(cos)
 

except Exception as e1 :
    print("e1=============", e1)
finally:
    driver.close()