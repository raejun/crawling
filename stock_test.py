import math
import time
import csv
import calendar
import codecs
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
from urllib.request import urlopen

def insert_data(cos):
    conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='cosdac', charset="utf8")
    cur = conn.cursor()
    sql = """ INSERT INTO cosdac(code,name,npr,op,creper,msh,mbh,tr_ct,tr_pr,tpr,hpr,lpr,acpr,money,tcoun,totpr,what)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(sql, cos)
    conn.commit()
    conn.close()

main_url = "http://marketdata.krx.co.kr/mdi#document=040602"
driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
time.sleep(3)
driver.find_element_by_css_selector("#market_gubun2a87ff679a2f3e71d9181a67b7542122c").click()
time.sleep(1)
ct1 = 1
year = 2018
month = 11
day = 30
ct = 15
wday = 5

li = []

while ct <= 18:
    f = open("holiday%s.csv" % ct, 'r')
    rdr = csv.reader(f)
    for line in rdr:
        li.append(line)
    ct += 1
    f.close()

while year >= 2015:
    day -= 1
    wday -= 1
    if day == 0:
        month -= 1
        if month == 0:
            year -=1
            if year == 14:
                break
            month = 12
        day = calendar.monthrange(year, month)[1]
    if wday == 0:
        wday = 7
        continue
    if wday == 6:
        continue
    
    if month < 10 and day < 10:
        date = str(year) + "0" + str(month) + "0" + str(day)
    elif day < 10:
        date = str(year) + str(month) + "0" + str(day)
    elif month < 10:
        date = str(year) + "0" + str(month) + str(day)
    else:
        date = str(year) + str(month) + str(day)

    if [date] in li:
        continue

    elem = driver.find_element_by_id("schdated3d9446802a44259755d38e6d163e820")
    elem.clear()
    elem.send_keys(date)
    driver.find_element_by_css_selector("#btnidc81e728d9d4c2f636f067f89cc14862c").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='6512bd43d9caa6e02c990b0a82652dca']/button[3]").click()
    time.sleep(2)
    li1 = []
    f = codecs.open("C:/Users/Playdata/Downloads/data (%s).csv" % ct1, 'r', 'utf-8')
    rdr = csv.reader(f)
    print(rdr)
    for line in rdr:
        if line[1] == "종목명":
            continue
        li1.append(line)
    f.close()
    ct1 += 1
    for cos in li1:
        insert_data(cos)


# def insert_lotto(lotto):
#     conn = pymysql.connect(host="localhost", user="root", password="1234",
#                         db='lotto', charset="utf8")
#     cur = conn.cursor()
#     sql = """ INSERT INTO lotto(count,number,win_count,win_money,lotto_date,twm)
#             VALUES(%s,%s,%s,%s,%s,%s)"""
#     cur.execute(sql, lotto)
#     conn.commit()
#     conn.close()

# try:
#     table = driver.find_element_by_tag_name('table')
#     tbody = table.find_element_by_tag_name("tbody")
#     trs = tbody.find_elements_by_tag_name("tr")
# except NoSuchElementException:
#     print(" [예외 발생] 표 없음 ")
# tabletrcount = 0
# for tr in trs:
#     if tabletrcount == 0 or tabletrcount == 11:
#         tabletrcount += 1
#         continue
#     else :
#         td = list(tr.find_elements_by_tag_name('td'))
#         count = td[0].text
#         print(count)
#         win_url = "http://nlotto.co.kr/gameResult.do?method=byWin&drwNo=%s" % count
#         win_html = urlopen(win_url)
#         win_soup = BeautifulSoup(win_html, "lxml")
#         win_hoi = win_soup.find('h3', {'class': 'result_title'})
#         win_body = win_hoi.find('span')
#         total_win_money = win_soup.find('span', {'class': 'f_blue'})
#         storeurl = "http://nlotto.co.kr/store.do?method=topStore&pageGubun=L645&drwNo=%s" % count
#         storehtml = urlopen(storeurl)
#         storesoup = BeautifulSoup(storehtml, "lxml")
#         storehoi = storesoup.find('table', {'class': 'tblType1'})
#         storebody = storehoi.find('tbody')
#         for tr1 in list(storebody.find_all('tr')):
#             if tr1.find('td',{'class':'tblType1line1'}) != None :
#                 continue
#             elif tr1.find('td',{'class':'tblType1line2'}) != None :
#                 continue
#             else :
#                 td2 = list(tr1.find_all('td'))
#                 sname = td2[1].text
#                 location = td2[3].text
#                 storedata.append([count, sname, location])
#         number = td[1].text
#         win_count = td[2].text
#         win_money = td[3].text
#         date = win_body.text
#         lotto_date = date[1:5] + "-" + date[7:9]
#         twm = total_win_money.text
#         lottodata.append([count, number, win_count, win_money, lotto_date, twm])
#         tabletrcount += 1
# pagecount += 1
# time.sleep(2)
# if pagecount+dif < 13:
#     driver.find_element_by_css_selector("#page_box > ul > li > span:nth-child(" + str(pagecount) + ") > a").click()
#     time.sleep(2)
# elif pagecount+dif == 13:
#     driver.find_element_by_css_selector("#page_box > ul > li > span:nth-child(" + str(pagecount) + ") > a > img").click()
#     time.sleep(2)
#     pagecount = 3
#     dif = 0
#     nextpage10 -= 1
# if nextpage10 == 0 and ((int(page)%10)+2 < (pagecount+dif)):
#     break