from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import os 

# 현재 스크립트 파일의 디렉토리 경로를 가져옴
current_directory = os.path.dirname(os.path.abspath(__file__))
image_folder = os.path.join(current_directory, "images")

# 폴더가 존재하지 않으면 생성
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

driver = webdriver.Chrome()
driver.get('https://pposong-k.tistory.com/321') # 게시물 주소
driver.implicitly_wait(15)

imageblocks = driver.find_elements(By.CLASS_NAME , 'imageblock')

for i in range(len(imageblocks)):
    image_span = imageblocks[i].find_element(By.TAG_NAME , 'span')
    # 이미지를 해당 폴더에 저장
    urllib.request.urlretrieve(image_span.get_attribute("data-url"), os.path.join(image_folder, f"{i}.png"))