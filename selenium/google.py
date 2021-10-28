from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# 조코딩 유튜브 강의를 보며 학습
# 파이썬 셀레니움 이미지 크롤링
# https://www.youtube.com/watch?v=1b7pXC1-IbE&list=PLU9-uwewPMe0ImjRBu-TLecU-LBhZvX2b&index=1&t=1588s


SCROLL_PAUSE_TIME = 1

# driver = webdriver.Chrome() 하니까 오류나서 아래 3줄로 바꿈
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.co.kr/imghp")  # google 이미지검색은 주소가 다르닷
elem = driver.find_element_by_name("q")
elem.send_keys("조코딩")
elem.send_keys(Keys.RETURN)  # 엔터키

# 페이지에 스크롤 다 내려서 모든 이미지 노출시킨 후 이미지 선택하기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:  # 스크롤 다 내렸을때 버튼 없을 때 빠져나가기
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")  # class는 연결을 . 으로 한다
count=1
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        # 특정 사이트의 경우 봇의 접근금지가되어 아래 3줄 추가 후(브라우저인것처럼 속임) 동작
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count +=1
    except:
        pass  # 오류나면 일단 넘어가고 다음라인 처리
driver.close()  # webdriver 종료