from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

import pandas as pd
import re

#I. Tạo nơi chứa links và tạo dataframe rỗng
all_links = []
d = pd.DataFrame({'Name of the band': [], 'Years active': []})
######################################################
# II. Lấy ra tất cả các đường dẫn để truy cập painters

# Khởi tạo Webdriver
driver = webdriver.Chrome()

# mở trang
url = 'https://en.wikipedia.org/wiki/Lists of musicians'
driver.get(url)

#dung 2s
time.sleep(2)

# lấy tất cả các thẻ ul
ul_tags = driver.find_elements(By.TAG_NAME, "ul")
print(len(ul_tags))

#chọn thẻ ul thứ 22
ul_artist = ul_tags[21]

#lay tat ca cac ther li owr trong ul
li_tags = ul_artist.find_elements(By.TAG_NAME, 'li')

#Tạo danh sách các url
links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]

#xuất thông tin
for link in links:
    print(link)

#truy cap den link dau tien cua A
url1 = driver.get(links[0])

# lấy tất cả các thẻ ul
ul1_tags = driver.find_elements(By.TAG_NAME, "ul")
print(len(ul1_tags))
#for index, value in enumerate(ul_tags):
    #print(f'Index: {index}, Value{value.text}')
# chọn thẻ ul thứ 22
ul_artist = ul1_tags[21]

# lay tat ca cac ther li owr trong ul
li1_tags = ul_artist.find_elements(By.TAG_NAME, 'li')

# Tạo danh sách các url
artist_links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li1_tags]
for link1 in artist_links:
    print(link1)
    driver.get(link1)
    time.sleep(2)
# laays teen ban nhac va nam hoat dong
    try:
        band_name = driver.find_element(By.TAG_NAME, "h1").text
    except:
        band_name = ""

    # lấy nam hoat dong
    try:
        years_active = driver.find_element(By.XPATH, "//th[span[text()='Years active']]/following-sibling::td")
        years_active = years_active.text
    except:
        years_active = ""
    #tạo dictionary  thong tin của họa sĩ
    artist = {'Name of the band': band_name, 'Years active': years_active}

    artist_df = pd.DataFrame([artist])

    d = pd.concat([d, artist_df], ignore_index=True)
print(d)

file_name = 'Musicians.xlsx'

# saving the Excel
d.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')


# đóng webdriver
driver.quit()
