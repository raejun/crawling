# 인터파크 투어 사이트에서 여행지를 입력후 검색 -> 잠시후 -> 결과
# conda install selenium
# conda install beautifulsoup4
# conda install pymysql
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# 명시적 대기를 위해
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# db       = Db()
main_url = 'http://tour.interpark.com/'
keyword  = '파리'
# 상품 정보를 담는 리스트 (TourInfo 리스트)
tour_list = []

driver = webdriver.Chrome(executable_path='C:/driver/chromedriver.exe')
driver.get(main_url)
# 검색창을 찾아서 검색어 입력
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
# 수정할경우 => 뒤에 내용이 붙어버림 => .clear() -> send_keys('내용')
# 검색 버튼 클릭
driver.find_element_by_css_selector('button.search-btn').click()

# 잠시 대기 => 페이지가 로드되고 나서 즉각적으로 데이터를 획득
# 명시적 대기 => 특정 요소가 로케이트(발결될 때까지) 대기
try:
    element = WebDriverWait(driver, 10).until(
        # 지정한 한개 요소가 올라오면 웨이트 종료
        EC.presence_of_element_located( (By.CLASS_NAME, 'oTravelBox') )
    )
except Exception as e:
    print( '오류 발생', e)
# 암묵적 대기 => DOM이 다 로드 될때까지 대기 하고 먼저 로드되면 바로 진행
# 요소를 찾을 특정 시간 동안 DOM 풀링을 지시 예를 들어 10 초 이내로 발견되면 진행
driver.implicitly_wait( 10 )
# 절대적인 대기 => time.sleep(10) -> 클라우드 페어(디도스 방어 솔루션)
# 더보기 눌러서 => 게시판 진입
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()

# 게시판 스캔 => 메타 정보 획득 => loop 를 돌려서 일괄적으로 방문 접근 처리
# searchModule.SetCategoryList(1, '') 스크립트 실행
# 16은 임시값, 게시물을 넘어갔을 때 현상을 확인
for page in range(1, 2):#16):
    try:
        # 자바스크립트 구동하기
        driver.execute_script("searchModule.SetCategoryList(%s, '')" % page)
        time.sleep(2)
        print("%s 페이지 이동" % page)
        #############################################################
        # 여러 사이트에서 정보를 수집할 경우 공통 정보 정의 단계 필요
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 썸네일, 링크(상품상세정보)
        boxItems = driver.find_elements_by_css_selector('div.panelZone > div.oTravelBox > ul > li')
        # 상품 하나 하나 접근
        for li in boxItems:
            print( '썸네임', li.find_element_by_css_selector('img').get_attribute('src') )
            print( '링크', li.find_element_by_css_selector('a').get_attribute('onclick') )
            print( '상품명', li.find_element_by_css_selector('h5.proTit').text )
            print( '코멘트', li.find_element_by_css_selector('.proSub').text )
            print( '가격',   li.find_element_by_css_selector('.proPrice').text )
            area = ''
            for info in li.find_elements_by_css_selector('.info-row .proInfo'):
                print(  info.text )
            print('='*100)
            # 데이터 모음
            # li.find_elements_by_css_selector('.info-row .proInfo')[1].text
            # 데이터가 부족하거나 없을수도 있으므로 직접 인덱스로 표현은 위험성이 있음
    except Exception as e1:
        print( '오류', e1 )

# 종료
driver.close()
driver.quit()

import sys
sys.exit()
