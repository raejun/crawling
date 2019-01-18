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
import os

def insert_data(rdr):
    conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='cosdac', charset="utf8")
    cur = conn.cursor()
    sql = """ INSERT INTO cosdac(code,name,npr,op,creper,msh,mbh,tr_ct,tr_pr,tpr,hpr,lpr,acpr,money,tcoun,totpr,what,date)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(sql, rdr)
    conn.commit()
    conn.close()

# li1 = []
f = codecs.open("C:/Users/Playdata/Downloads/total.csv", 'r', 'utf-8')
rdr = csv.reader(f)
print(rdr)
# for line in rdr:
#    if line[1] == "종목명":
#        continue
#    line.append(date)
#    li1.append(line)
# f.close()
# os.remove("C:/Users/Playdata/Downloads/data.csv")
# for cos in li1:
insert_data(rdr)