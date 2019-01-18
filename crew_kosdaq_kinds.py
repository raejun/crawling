import math
import time
import codecs
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
from selenium.webdriver.chrome.options import Options


def insert_data(kos):
    conn = pymysql.connect(host="localhost", user="root", password="qkr402",
                        db='stock', charset="utf8")
    curs = conn.cursor()
    sql = """ INSERT INTO kosdaq_kind(code,kind)
            VALUES(%s,%s)"""
    curs.execute(sql, kos)
    conn.commit()
    conn.close()

conn = pymysql.connect(host="localhost", user="root", password="qkr402",
                        db='stock', charset="utf8")
curs = conn.cursor()
sql = """ select code from kosdac where date = '20181129';"""
curs.execute(sql)
rows = curs.fetchall()
cosdaq_name = []
for i in rows:
    # print(i)
    i = str(i)
    # print(type(i))
    i = i.replace("('", "")
    i = i.replace("',)", "")
    # print(i)
    cosdaq_name.append(i)
conn.close()
# print(cosdaq_name)

main_url = "https://finance.naver.com/"
# driver = webdriver.Chrome("C:/driver/chromedriver.exe")

options = Options()
options.add_argument('--no-sandbox') # Bypass OS security model
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
driver.get(main_url)
time.sleep(3) # 무조건 정해진 시간(초) 쉰다.
p = 0
kosdaq_kinds = []
for code in cosdaq_name:
    elem = driver.find_element_by_id('stock_items')
    elem.clear()
    elem.send_keys(code)
    click = driver.find_element_by_class_name('snb_search_btn').click()
    time.sleep(1)
    # kinds_choice = driver.find_element_by_css_selector('#boxTabs > td:nth-child(7) > a').click()
    # time.sleep(5)
    kinds = "";
    try:
        kinds = driver.find_element_by_css_selector('#content > div.section.trade_compare > h4 > em > a')
        kind = kinds.text
        # print(kind)
        kosdaq_kinds.append(code)
        kosdaq_kinds.append(kind)
        print(kosdaq_kinds)
        print(type(code))
        print(type(kind))
        print(type(kosdaq_kinds))
        p += 1
        print(p)
    except Exception as e1 :
        print("e1=============", e1)
    for kos in kosdaq_kinds : 
        insert_data(kos)
        print("저장완료")
driver.close()