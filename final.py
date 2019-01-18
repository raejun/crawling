import time
import math
import pymysql
from bs4 import BeautifulSoup

from selenium import webdriver


# https://selenium-python.readthedocs.io/waits.html#explicit-waits 코드를 복사
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


main_url = "http://www.gunsys.com/q/index.php?currentPage={}&bigCode=10&midCode=1010&smallCode="

# options = Options()
# options.add_argument('--no-sandbox') # Bypass OS security model
# driver1 = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
# driver2 = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
# driver3 = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
# driver4 = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
# driver5 = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
# driver6 = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
# driver7 = webdriver.Chrome(chrome_options=options, executable_path=r'C:\driver/chromedriver.exe')
# time.sleep(3) # 무조건 정해진 시간(초) 쉰다.

driver1 = webdriver.Chrome("C:/driver/chromedriver.exe")
# driver2 = webdriver.Chrome("C:/driver/chromedriver.exe")
# driver3 = webdriver.Chrome("C:/driver/chromedriver.exe")
# driver4 = webdriver.Chrome("C:/driver/chromedriver.exe")
# driver5 = webdriver.Chrome("C:/driver/chromedriver.exe")
# driver6 = webdriver.Chrome("C:/driver/chromedriver.exe")
# driver7 = webdriver.Chrome("C:/driver/chromedriver.exe")

time.sleep(3) # 무조건 정해진 시간(초) 쉰다.

Auction_list = []
def insert_auction(auction):
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='auction', charset='utf8')
    cur = conn.cursor()
    sql = """INSERT INTO apart1_auction(str_link, str_land_num, str_land_type, str_land_area, str_land_surface, str_land_site, str_land_high_price, str_land_low_price, str_land_condition, str_land_date, str_land_count) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute( sql, auction )
    conn.commit()
    conn.close()
    print("저장 성공!")

try:
    for page in range(1, 4):
        driver1.get("http://www.gunsys.com/q/index.php?currentPage={}&bigCode=10&midCode=1010&smallCode=".format(page))
        time.sleep(2)
        for test in range(2, 22):
            test_num = driver1.find_element_by_css_selector("#body_style > div > div > div > div > table:nth-child(2) > tbody > tr:nth-child({}) > td:nth-child(5) > a".format(test)).click()
            print("페이지는 {}입니다.".format(test))
            time.sleep(2)
            test_next = [2,4,6]
            
        # for test1_class in range(2, 7):
            test_class1 = driver1.find_element_by_xpath('//*[@id="index_div"]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[4]/a').click()
            print("페이지는 1과목입니다.")
            time.sleep(3)
            for i, x in zip(test_next, range(0,4)):
            # 문제 번호 추출

                test_class1_num1 = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td[1]'.format(x))
                str_test_class1_num1 = test_class1_num1.text
                print(str_test_class1_num1)
                int_test_class1_num1 = str_test_class1_num1.replace(".","")
                int_test_class1_num1 = int(int_test_class1_num1)
                print(int_test_class1_num1)
                test_class1_num2 = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[1]'.format(x))
                str_test_class1_num2 = test_class1_num2.text
                print(str_test_class1_num2)
                int_test_class1_num2 = str_test_class1_num2.replace(".","")
                int_test_class1_num2 = int(int_test_class1_num2)
                print(int_test_class1_num2)
                test_class1_num3 = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[3]/tbody/tr[1]/td[1]'.format(x))
                str_test_class1_num3 = test_class1_num3.text
                print(str_test_class1_num3)
                int_test_class1_num3 = str_test_class1_num3.replace(".","")
                int_test_class1_num3 = int(int_test_class1_num3)
                print(int_test_class1_num3)

                test_class1_num4 = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[2]/table[1]/tbody/tr[1]/td[1]'.format(x))
                str_test_class1_num4 = test_class1_num4.text
                print(str_test_class1_num4)
                int_test_class1_num4 = str_test_class1_num4.replace(".","")
                int_test_class1_num4 = int(int_test_class1_num4)
                print(int_test_class1_num4)
                test_class1_num5 = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[1]'.format(x))
                str_test_class1_num5 = test_class1_num5.text
                print(str_test_class1_num5)
                int_test_class1_num5 = str_test_class1_num5.replace(".","")
                int_test_class1_num5 = int(int_test_class1_num5)
                print(int_test_class1_num5)
                print(type(int_test_class1_num5))
            
            # 문제 추출
                test_class1_num1_title = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td[2]'.format(x))
                str_test_class1_num1_title = test_class1_num1_title.text
                print(str_test_class1_num1_title)
                test_class1_num2_title = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]'.format(x))
                str_test_class1_num2_title = test_class1_num2_title.text
                print(str_test_class1_num2_title)
                test_class1_num3_title = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[3]/tbody/tr[1]/td[2]'.format(x))
                str_test_class1_num3_title = test_class1_num3_title.text
                print(str_test_class1_num3_title)
                
                test_class1_num4_title = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[2]/table[1]/tbody/tr[1]/td[2]'.format(x))
                str_test_class1_num4_title = test_class1_num4_title.text
                print(str_test_class1_num4_title)
                test_class1_num5_title = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td[2]'.format(x))
                str_test_class1_num5_title = test_class1_num5_title.text
                print(str_test_class1_num5_title)

            # 문제 이미지 추출 (test 해봐야됨, null값 조정)
                test_class1_num1_img = ""; test_class1_num2_img = ""; test_class1_num3_img = ""; test_class1_num4_img = ""; test_class1_num5_img = "";
                try:
                    test_class1_num1_img = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[1]/tbody/tr[1]/td[2]/img'.format(x))
                    str_test_class1_num1_img = test_class1_num1_img.text
                    print(str_test_class1_num1_img)
                except Exception as e1_img :
                    print("e1_img=============", e1_img)

                try:
                    test_class1_num2_img = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/img'.format(x))
                    print(test_class1_num2_img)
                    str_test_class1_num2_img = test_class1_num2_img.text
                    print(str_test_class1_num2_img)
                    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                except Exception as e1_img :
                    print("e1_img=============", e1_img)

                try:    
                    test_class1_num3_img = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[1]/table[3]/tbody/tr[1]/td[2]/img'.format(x))
                    str_test_class1_num3_img = test_class1_num3_img.text
                    print(str_test_class1_num3_img)
                except Exception as e1_img :
                    print("e1_img=============", e1_img)
                try:
                    test_class1_num4_img = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[2]/table[1]/tbody/tr[1]/td[2]/img'.format(x))
                    str_test_class1_num4_img = test_class1_num4_img.text
                    print(str_test_class1_num4_img)
                except Exception as e1_img :
                    print("e1_img=============", e1_img)
                try:
                    test_class1_num5_img = driver1.find_element_by_xpath('//*[@id="div0{}"]/table[1]/tbody/tr/td[2]/table[1]/tbody/tr[1]/td[2]/img'.format(x))
                    str_test_class1_num5_img = test_class1_num5_img.text
                    print(str_test_class1_num5_img)
                except Exception as e1_img :
                    print("e1_img=============", e1_img)
                
                num_table = list()
                num_table.append(int_test_class1_num1)
                num_table.append(int_test_class1_num2)
                num_table.append(int_test_class1_num3)
                num_table.append(int_test_class1_num4)
                num_table.append(int_test_class1_num5)
                print(num_table)
                print(type(num_table))
            
            # 문제 보기 추출(테스트 해봐야됨, {}안에 문제)
                test_class1_num1_choice = ""; test_class1_num1_choice_img = "";
                try:
                    for s in num_table:
                        try:
                            test_class1_num1_choice = driver1.find_element_by_id('quesitem{}1'.format(s))
                            str_test_class1_num1_choice = test_class1_num1_choice.text
                            print(str_test_class1_num1_choice)
                        except Exception as choice :
                            print("choice=============", choice)
                        try:
                            test_class1_num2_choice = driver1.find_element_by_id('quesitem{}2'.format(s))
                            str_test_class1_num2_choice = test_class1_num2_choice.text
                            print(str_test_class1_num2_choice)
                        except Exception as choice :
                            print("choice=============", choice)    
                        try:
                            test_class1_num3_choice = driver1.find_element_by_id('quesitem{}3'.format(s))
                            str_test_class1_num3_choice = test_class1_num3_choice.text
                            print(str_test_class1_num3_choice)
                        except Exception as choice :
                            print("choice=============", choice)    
                        try:    
                            test_class1_num4_choice = driver1.find_element_by_id('quesitem{}4'.format(s))
                            str_test_class1_num4_choice = test_class1_num4_choice.text
                            print(str_test_class1_num4_choice)
                        except Exception as choice :
                            print("choice=============", choice)
                        try:
                            test_class1_num1_choice_img = driver1.find_element_by_xpath('//*[@id="quesitem{}1"]/a/img'.format(s))
                            str_test_class1_num1_choice_img = test_class1_num1_choice_img.text
                            print(str_test_class1_num1_choice_img)
                        except Exception as choice_img :
                            print("choice_img=============", choice_img)
                        try:
                            test_class1_num2_choice_img = driver1.find_element_by_xpath('//*[@id="quesitem{}2"]/a/img'.format(s))
                            str_test_class1_num2_choice_img = test_class1_num2_choice_img.text
                            print(str_test_class1_num2_choice_img)
                        except Exception as choice_img :
                            print("choice_img=============", choice_img)
                        try:
                            test_class1_num3_choice_img = driver1.find_element_by_xpath('//*[@id="quesitem{}3"]/a/img'.format(s))
                            str_test_class1_num3_choice_img = test_class1_num3_choice_img.text
                            print(str_test_class1_num3_choice_img)
                        except Exception as choice_img :
                            print("choice_img=============", choice_img)
                        try:
                            test_class1_num4_choice_img = driver1.find_element_by_xpath('//*[@id="quesitem{}4"]/a/img'.format(s))
                            str_test_class1_num4_choice_img = test_class1_num4_choice_img.text
                            print(str_test_class1_num4_choice_img)
                        except Exception as choice_img :
                            print("choice_img=============", choice_img)        
                        print("여기까지는 됨!")
                        
                except Exception as c1 :
                    print("c1=============", c1)
            # 다음 페이지 테스트 해봐야됨
                print("여기까지는 됨!")
                test_next_click = driver1.find_elements_by_class_name("btn01_qpass")
                print(test_next_click[i])
                print(i)
                test_next_click1 = test_next_click[i]
                test_next_click1.click()
                time.sleep(3)
                print("여기까지는 됨!")
            
                
                
                
                
                # test_next = driver.find_element_by_xpath('//*[@id="div01"]/table[2]/tbody/tr/td[2]/input')
                # text_next = driver.find_element_by_class_name("btn01_qpass").click()
                # test_next = driver.find_element_by_css_selector('#div00 > table:nth-child(2) > tbody > tr > td:nth-child(2) > input').click()
            #driver.find_element_by_xpath('//*[@id="body_style"]/div/div/div/div[2]/table[1]/tbody/tr/td[2]/input').click()
            #driver.back()
except Exception as e1 :
    print("e1=============", e1)
finally:
    driver1.close()