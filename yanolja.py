import time
import math
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pymysql

main_url = "https://www.yanolja.com/"
driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver2 = webdriver.Chrome("C:/driver/chromedriver.exe") 
driver.get(main_url)
driver.implicitly_wait(10)

def insert_tour(tour):
    conn = pymysql.connect(host="localhost", user="root", password="1234",
                        db='test', charset="utf8mb4")
    cur = conn.cursor()
    sql = """ INSERT INTO yanolja3(date, address, phone, num_hugi, title, max_daesil_time, daesil_price, sukbak_time, sukbak_price, hashtag, content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)"""
    cur.execute(sql, tour)
    conn.commit()
    conn.close()

    print("저장 성공!!!")

# 1. 도 별로!

loc_btn = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section/div[1]/div/div/div[2]/span/div/div/div[1]/button')
loc_btn.click()

data = [] # 총 데이터 담는 이중리스트

#시도 이름  
loc_area = driver.find_element_by_css_selector("#main > article > div > div:nth-child(1) > section > div.search-panel.column1 > div > div > div.option-item.item-option-area > span > div > div > div.popover-content.popover-search-option.animate-bounce-down > div > div > div")
locations = loc_area.find_elements_by_tag_name("li")

for i, loc in enumerate(locations):  # i : 서울 각 구

    print("{}번째 목록".format(i+1))
    #loc_btn 계속 재정의해주지않으면 에러남!
    loc_btn = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section/div[1]/div/div/div[2]/span/div/div/div[1]/button')
    time.sleep(2)
    if i != 0:
        loc_btn.click()  
    # 18.11.12 -> XPath 는 갓입니다!
    time.sleep(2)
    loc_link = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section/div[1]/div/div/div[2]/span/div/div/div[2]/div/div/div/ul/li[%s]/a' % str(i+1) )
    location_name = loc_link.text # 강남/역삼/삼성/논현
    
    loc_link.click()
    time.sleep(2)
    
    #날짜 입력 버튼
    
    for j in range(7,8): # j로 날짜 조절!
        check_in = driver.find_element_by_xpath('//*[@id="startDate"]')
        date = check_in.text
        
        time.sleep(2)
        check_in.click()
        time.sleep(2)
        check_in_date = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section/div[1]/div/div/div[3]/div[2]/div/div/div/div/div[2]\
                                                     /div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[3]/td[%s]/button' % str(j))
        
        time.sleep(2)
        check_in_date.click()
        time.sleep(2)
        ok_button = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section/div[1]/div/div/div[3]/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        ok_button.click()
    
        time.sleep(5)
        # 숙소검색 버튼 입력 
        search_btn = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section/div[1]/div/button')
        #driver.execute_script("document.querySelector('a.terms').click();")
        time.sleep(2)
        if search_btn:
            print("btn click")
            search_btn.click()
        else:
            print("btn noooooooooooooooooo")

        time.sleep(2)
        
        # 세부 페이지로 들어감!
        elm = driver.find_element_by_tag_name('html')
        for i in range(6):
            elm.send_keys(Keys.END)
            time.sleep(1)

        k = 0
        error_num = 0 # while문 빠져나오기 위해 도입

        placelist_container = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section[4]/div/div[2]')
        while(True):
            try: # 지역 추천이 있는 페이지, 없는 페이지가 있음 -> 모든 경우 만족시키기 위한 try문
                premium_list = placelist_container.find_element_by_xpath('//*[@id="main"] \
                                                                              /article/div/div[1]/section[4]/div/div[2]\
                                                                             /div[%s]/ul' % (str(k+1))).find_elements_by_tag_name("li")
            except:
                error_num += 1
                print("지역 추천은 DB에 안넣을거야!!")
                if error_num >= 2:
                    break
                else:
                    k += 1
                    continue

            for m, each_list in enumerate(premium_list):

                str_title = ""; num_hugi =""; max_daesil_time=""; daesil_price=""; sukbak_time=""; sukbak_price="";
                has_class=""; hashtag=""; content="";

                address = ""; phone_num = "";

                image_box = each_list.find_element_by_class_name("image-box").find_element_by_tag_name("a")
                link = image_box.get_attribute("href")


                driver2.get(link)

                try:
                    time.sleep(2)
                    address = driver2.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/div[2]/div[1]/section[1]/\
                                                            div[1]/div[1]/div[1]').text
                    phone_num = driver2.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/div[2]/div[1]/section[1]/\
                                                            div[1]/div[1]/div[2]').text
                except:
                    print("phone_num, address오류")
                

                # 각 요소가 없을 때 예외처리
                # 제목
                time.sleep(2)
                str_title = each_list.find_element_by_class_name("title-text").text

                try: # 후기 갯수
                    num_hugi = each_list.find_element_by_class_name("score-rap").find_element_by_class_name("txt-review").text
                    num_hugi = num_hugi.replace("후기 : ", "").replace("개", "")
                except:
                    print("후기 갯수가 없습니다!")
                try: # 최대 대실시간
                    max_daesil_time = each_list.find_elements_by_class_name("price-type")[0].find_element_by_tag_name("small").text
                    max_daesil_time = max_daesil_time.replace("최대 ", "").replace("시간", "")
                except:
                    print("최대 대실 시간이 없습니다.")
                try:# 대실 가격
                    daesil_price = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section[4]/div/div[2] \
                                                                   /div[%s]/ \
                                                                   ul/li[%s]/div/div[2]/div[3]/div[1]/span/span/em[2]'
                                                                   % (str(k+1), str(m+1))).text
                    daesil_price = daesil_price.replace("원", "")
                except:
                    print("대실 가격이 없습니다.")

                try: # 숙박 시간(몇 시부터 숙박 가능!)
                    sukbak_time = each_list.find_elements_by_class_name("price-type")[1].find_element_by_tag_name("small").text
                    sukbak_time = sukbak_time.replace(" ~", "")
                except:
                    print("숙박 시간이 없습니다.")
                try: # 숙박 가격
                    sukbak_price = driver.find_element_by_xpath('//*[@id="main"]/article/div/div[1]/section[4]/div/div[2] \
                                                                   /div[%s]/ \
                                                                   ul/li[%s]/div/div[2]/div[3]/div[2]/span/span/em[2]'
                                                                   % (str(k+1), str(m+1))).text
                    sukbak_price = sukbak_price.replace("원", "")
                except:
                    print("숙박 가격이 없습니다.")
                try: 
                    hash_class = each_list.find_element_by_class_name('hashtag-rap')
                    # 해시태그 정보
                    hashtag = hash_class.find_element_by_tag_name('em').text
                except:
                    print("해시태그가 없습니다.")
                try:
                    temp = hash_class.find_elements_by_tag_name('p')
                    for com in temp:
                        content += com.text
                except:
                    print("내용이 없습니다.")
                each_data = ['2018-11-17', address, phone_num ,num_hugi, str_title, max_daesil_time, daesil_price, sukbak_time, sukbak_price, hashtag, content]
                print(each_data)
                insert_tour(each_data)
            
            k += 1

        data.append(each_data)
        driver.back()
        print("driver.back()")

print("end")
driver2.close()
driver.close()

