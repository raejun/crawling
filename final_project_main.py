import time

import pymysql

from selenium import webdriver

 

driver = webdriver.PhantomJS('phantomjs')    # use phantomjs driver 

 

try:

    for page1 in range(1,4):    # page 1 ~ 3

        driver.get("http://www.gunsys.com/q/index.php?currentPage={}&bigCode=10&midCode=1010&smallCode=".format(page1))

 

        for page2 in range(2, 22): # '응시하기', page마다 20개의 시험 존재

            btn_click = driver.find_element_by_css_selector("#body_style > div > div > div > div > table:nth-child(2) > tbody > tr:nth-child({}) > td:nth-child(5) > a".format(page2)).click()    # 버튼 클릭

 

            for page3 in range(2, 7): # 과목 선택 1과목 ~ 5과목

                btn_click = driver.find_element_by_xpath('//*[@id="index_div"]/table/tbody/tr[3]/td/table/tbody/tr[{}]/td[4]/a'.format(page3)).click()    # 각 과목버튼 클릭

 

                for page4 in range(0, 4): # 각 과목의 시험 페이지 수, 4장 0 ~ 3

                    

                    for page5 in range(1, 6): # 문제 내용 1,2,3 -> 왼 / 4,5 -> 오

                        if page5 < 4:    # 1,2,3 -> 왼

                            temp_num = driver.find_element_by_xpath('//*[@id="div{}{}"]/table[1]/tbody/tr/td[1]/table[{}]/tbody/tr[1]/td[1]'.format(page3-2,page4,page5))

 

                            temp_title = driver.find_element_by_xpath('//*[@id="div{}{}"]/table[1]/tbody/tr/td[1]/table[{}]/tbody/tr[1]/td[2]'.format(page3-2,page4,page5))

 

 

                            try:

                                p_image = driver.find_element_by_xpath('//*[@id="div{}{}"]/table[1]/tbody/tr/td[1]/table[{}]/tbody/tr[1]/td[2]/img'.format(page3-2,page4,page5)).get_attribute('src')

 

                            except Exception as e :

                                p_image = None

                                pass

 

                            

                        else:

                            temp_num = driver.find_element_by_xpath('//*[@id="div{}{}"]/table[1]/tbody/tr/td[2]/table[{}]/tbody/tr[1]/td[1]'.format(page3-2,page4,page5-3)) 

 

                            temp_title = driver.find_element_by_xpath('//*[@id="div{}{}"]/table[1]/tbody/tr/td[2]/table[{}]/tbody/tr[1]/td[2]'.format(page3-2,page4,page5-3))

                            try:

                                p_image = driver.find_element_by_xpath('//*[@id="div{}{}"]/table[1]/tbody/tr/td[2]/table[{}]/tbody/tr[1]/td[2]/img'.format(page3-2,page4,page5-3)).get_attribute('src')

 

                            except Exception as e1_img :

                                p_image = None

                                pass

                    

                        if(p_image == None):    # 이미지 있는지 없는지 여부

                            p_conf = 0

                        else:

                            p_conf = 1

                        p_num = int((temp_num.text).rstrip('.'))    # '.'을 제외 한 후 int type으로 변경

                        p_title = temp_title.text    # 시험 문제 제목

                        yearhoi = driver.find_element_by_xpath('//*[@id="body_style"]/div/div/div/div[2]/table[1]/tbody/tr/td[1]').text     # "정보처리기사 필기 (2018년 2회 기출문제) 응시 Timer 0분 2초" year, hoi 뽑아내기 위함

                        

                        year1 = yearhoi.split(" (")

                        year2 = year1[1].split("년")

                        year = year2[0]

                        p_year = int(year)

 

                        hoi1 = yearhoi.split("년")

                        hoi2 = hoi1[1].split("회")

                        hoi = hoi2[0]

                        p_hoi = int(hoi)

                        

                        if((p_num) / 20 <= 1):

                            p_class = 1

                        elif((p_num) / 40 <= 1):

                            p_class = 2

                        elif((p_num) / 60 <= 1):

                            p_class = 3

                        elif((p_num) / 80 <= 1):

                            p_class = 4

                        else:

                            p_class = 5

                        

                        p_url = driver.current_url

 

                        print("p_year : ",p_year, "p_hoi : ",p_hoi,"p_class : ",p_class, "p_num : ",p_num, "p_url : ",p_url, "p_title : ",p_title, "p_conf : ",p_conf, "p_image",p_image)

                        

                        conn = pymysql.connect(host='192.168.113.4', user='root', password='1234', db='final_project', charset='utf8')

                        cur = conn.cursor()

                        sql = """insert into problem_main(p_year,p_hoi,p_class,p_num,p_url,p_title,p_conf,p_image,p_type,p_percent,p_answer) values(%s,%s,%s,%s,%s,%s,%s,%s,0,0,0)"""

                        

                        cur.execute( sql,(p_year,p_hoi,p_class,p_num,p_url,p_title,p_conf,p_image))

                        conn.commit()

                        conn.close()

                        print("저장 성공!!!")

                            

                    if(page4 != 3):    # 마지막페이지 다음 누르면 에러뜨기 때문

                        btn_click = driver.find_element_by_xpath('//*[@id="div{}{}"]/table[2]/tbody/tr/td[2]/input'.format(page3-2,page4)).click()

 

                btn_click = driver.find_element_by_xpath('//*[@id="body_style"]/div/div/div/div[2]/table[1]/tbody/tr/td[2]/input').click()    # 다음 과목으로 넘어가기 위하여 '첫화면' 버튼 클릭

 

            time.sleep(5)

            print("-----------------------",page2,"-------------------")

            driver.back()

 

except Exception as e :

    print("error = ", e)

finally:

    driver.close()