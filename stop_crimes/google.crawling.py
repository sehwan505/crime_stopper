from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import csv

# https://gist.github.com/aclisp/0c2965af80816bd332b7096a89908ef6 참고함
# 너무 로딩이 안되니까 youtube data api v3 를 써야겠다.
youtube_data = [] #데이터 저장 리스트


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito") #시크릿창으로 열기
# chrome_options.add_argument("headless") #창을 안열고 백그라운드에서 돌리기
# chrome_options.add_argument("window-size=1920x1080")


driver = webdriver.Chrome('C:/Users/sehwa/Downloads/chromedriver_win32/chromedriver.exe',options=chrome_options)
driver.get("https://www.google.com")
print("enter " + driver.title)
time.sleep(5)

search = driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
search.click()
search.send_keys("자영이란")
search.submit()
time.sleep(5)

page = driver.page_source
soup = BeautifulSoup(page,'lxml')

# b=soup.find_all('a')
# urls=[b[n].string for n in range(0,len(b))]
# print(b)

c=soup.find_all(attrs={'class':'LC20lb DKV0Md'})
titles=[c[n].string for n in range(0,len(c))]
print(titles)

textlist=[]
urls=[]

for i in range(0,len(titles)-1):
    item = driver.find_elements_by_css_selector('div.r > a')
    print(item)
    item[i].click()
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(4)

    print(item[i].get_attribute('href'))

    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    text = soup.find("body").text
    textcmt = re.sub('[/\r|\n/g]', '', text)
    textcmt = textcmt.split(' ')
    textlist.append(textcmt)
    print(textlist)

    driver.back()
time_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
textcsv = pd.DataFrame([pd.Series(text) for text in textlist ])
textcsv.to_csv(f'{time_now} google_data.csv', index=0, encoding="utf-8")

csvfile = open("google.title.csv","w",newline="", encoding="UTF-8")
csvwriter = csv.writer(csvfile)
for title,url in zip(titles,urls):
    try:
        csvwriter.writerow([title,url]) #이거 리스트 처리해야 한글자씩 안들어감
    except UnicodeEncodeError:
        pass

csvfile.close()