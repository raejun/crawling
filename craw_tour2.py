# craw_tour.py
# pip install BeautifulSoup4
# pip install selenium
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_url = "http://tour.interpark.com/"
keyword = "파리"

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
# time.sleep(3)  # 절대적 : 무조건 정해진 시간(초)를 쉰다.
driver.implicitly_wait(10) # seconds

# 입력란 찾기 <input id="SearchGNBText" ... >
elem = driver.find_element_by_id("SearchGNBText")
elem.clear()
elem.send_keys(keyword)
# elem.submit() <== 작동이 안됨! 이유 : 자바스크립트를 호출해야 검색이 됨!!!

# 검색 버튼 찾기 <button class="search-btn" ... >
btn_search = driver.find_element_by_css_selector("button.search-btn")
btn_search.click()

# 명시적 : 특정한 자원을 얻으면 바로 진행
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oTravelBox"))
    )
except Exception as e:
    print("명시적 대기 중 에러", e)

driver.find_element_by_css_selector("div.oTravelBox > ul > li.moreBtnWrap > button").click()

# 묵시적 : 페이지가 다 뜨면 진행
driver.implicitly_wait(10) # seconds

for page in range(1,2):
    try:
        # 자바스크립트 실행
        driver.execute_script("searchModule.SetCategoryList({}, '')".format(page))
        driver.implicitly_wait(5)
        print("{} 페이지로 이동!!!".format(page))
        soup = BeautifulSoup( driver.page_source, "lxml" )
        boxItems = soup.select(".panelZone > .oTravelBox > .boxList > .boxItem")
        # print(boxItems)
        for boxItem in boxItems:
            img_src = boxItem.find("img")['src']
            link = boxItem.find("a")['onclick']
            proTitle = boxItem.find("img")['alt']
            proComment = boxItem.find("p", {"class":"proSub"}).text
            # select 는 하나라도 리스트로 리턴
            proPrice = boxItem.select(".proPrice")[0].text
            proPrice = proPrice.replace(" ", "")
            proPrice = proPrice.replace("\n", "")
            tag_period = boxItem.select(".proInfo")[0]
            tag_period.find('span').replace_with('')  # <span> 태그 없애기
            proPeriod = tag_period.text
            proJumsu = boxItem.select(".proInfo")[2].text
            print("썸네일=", img_src)
            print("링크=", link)
            print("상품명=", proTitle)
            print("코멘트=", proComment)
            print("가격=", proPrice)
            print("여행기간=", proPeriod)
            print("평점=", proJumsu)
            print("=" * 100)  # ===...=== (= 100 개)
    except Exception as e:
        print("페이지 파싱 에러", e)
    finally:
        time.sleep(3)
        driver.close()
