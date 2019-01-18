# craw_tour.py
# pip install BeautifulSoup4
# pip install selenium
import math
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql

main_url = "http://tour.interpark.com/"
keyword = "파리"

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
# time.sleep(3)  # 절대적 기다리기 : 무조건 정해진 시간(초)를 쉰다.
driver.implicitly_wait(10) # 묵시적 기다리기

# 입력란 찾기 <input id="SearchGNBText" ... >
elem = driver.find_element_by_id("SearchGNBText")
elem.clear()
elem.send_keys(keyword)  # 파리
# elem.submit() <== 작동이 안됨! 이유 : 자바스크립트를 호출해야 검색이 됨!!!

# 검색 버튼 찾기 <button class="search-btn" ... >
btn_search = driver.find_element_by_css_selector("button.search-btn")
btn_search.click()

# 명시적 기다리기 : 특정한 자원을 얻으면 바로 진행
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oTravelBox"))
    )
except Exception as e:
    print("명시적 대기 중 에러", e)

driver.find_element_by_css_selector("div.oTravelBox > ul > li.moreBtnWrap > button").click()
time.sleep(3)

span_obj = driver.find_element_by_css_selector("div.panelZone > div.oTravelBox > h4 > span")
str_number = span_obj.text
str_number = str_number.replace("(", "")
str_number = str_number.replace(")", "")
number = int(str_number)
end = math.ceil(number / 10)  # 올림!!!

tour_list = []

# 함수 insert_tour 정의
def insert_tour(tour):
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='pythonDB', charset='utf8')
    cur = conn.cursor()
    sql = """INSERT INTO tbl_tour(title,link,img,comments,period,depart,price,score,reservation,feature)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute( sql, tour )
    conn.commit()
    conn.close()
    print("저장 성공!!!")


try:
    for page in range(1, end+1):
    # for page in range(1, 2):  # 테스트 용
        try:
            # 자바스크립트 실행
            driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))
            # 에러 !!!!!!!
            # driver.implicitly_wait(5)  # <== 반복문 안에서는 사용하지 말 것!!!
            # 이유 : 반복문 안에서 너무 빨리 작동되어 페이지 로드를 완료 못함!!! ㅠㅠ
            time.sleep(2)
            print("{} 페이지".format(page))
            boxItems = driver.find_elements_by_css_selector("div.panelZone > div.oTravelBox > ul > li")  # 여러 개 : .. s ...
            # print( len(boxItems) )  # 10
            # print( boxItems )  # 10개의 리스트 객체 출력됨!!!
            # 하나씩 처리
            for li in boxItems:
                # <a onclick="???" >
                a_obj = li.find_element_by_css_selector("a")
                str_onclick = a_obj.get_attribute("onclick")
                l_list = str_onclick.split(",")
                str_link = l_list[0]
                str_link = str_link.replace("searchModule.OnClickDetail('", "")
                str_link = str_link.replace("'", "")
                # <img src="???" >
                img = li.find_element_by_css_selector("img")
                str_img_src = img.get_attribute("src")
                proTit = li.find_element_by_css_selector(".proTit")
                str_title = proTit.text
                proSub = li.find_element_by_css_selector(".proSub")
                str_comment = proSub.text
                proInfos = li.find_elements_by_css_selector(".proInfo") # s
                obj_period = proInfos[0]
                str_period = obj_period.text
                obj_start = proInfos[1]
                str_start = obj_start.text
                proPrice = li.find_element_by_css_selector(".proPrice")
                str_price = proPrice.text
                proInfo = li.find_element_by_css_selector("div.info-row > div:nth-child(2) > p:nth-child(2)")
                str_score = proInfo.text
                # 여행정보
                tour = [str_title, str_link, str_img_src, str_comment, str_period, str_start, str_price, str_score]
                # 여행리스트에 담는다.
                tour_list.append(tour)
        except Exception as e:
            print("페이지 파싱 에러", e)
    # for 1 end

    for tour in tour_list:
        # print(tour)
        link = tour[1]
        print(link)
        driver.get(link)
        time.sleep(2)
        soup = BeautifulSoup( driver.page_source, "lxml" )
        trs = soup.select("table.ui-data-table > tbody > tr")  # select는 결과가 하나여도 리스트를 리턴
        tr2 = trs[2]
        td = tr2.find("td")
        # td 에는 [<strong>예약 0명</strong>, <br/>, ' (총 예정인원 10명 / 최소출발 2명)'] 로 저장된 상태
        strong = td.contents[0]  # <strong>예약 0명</strong>
        str_reservation = strong.string  # 예약 0명
        aaa = td.contents[2]  # ' (총 예정인원 10명 / 최소출발 2명)'
        str_reservation = str_reservation + aaa
        # print(str_reservation)  # 예약 0명 (총 예정인원 10명 / 최소출발 2명)
        tour.append(str_reservation)
        lis = soup.select(".goods-point > .ui-con-list > li")
        # print(lis)
        str_feature = ""
        for li in lis:
            str_feature = str_feature + li.string + " "
        tour.append(str_feature)
        # 데이터베이스에 저장
        insert_tour(tour)
    # for 2 end
    print( tour_list )
    print( len(tour_list) )
finally:
    driver.close()

# str_title, str_link, str_img_src, str_comment, str_period, str_start, str_price, str_score, str_reservation, str_feature

"""
create table tbl_tour(
	num int not null auto_increment,
	title varchar(100),
	link varchar(200),
	img varchar(200),
	comments varchar(100),
	period varchar(50),
	depart varchar(50),
	price varchar(50),
	score varchar(10),
	reservation varchar(50),
	feature varchar(200),
	primary key(num)
) COLLATE='utf8mb4_unicode_ci';
"""
