from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

######################################################
# I. Tạo nơi chứa links và tạo dataframe rỗng
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})
######################################################
# II. Lấy ra tất cả các đường dẫn để truy cập painters
# Khởi tạo Webdriver
for i in range(65, 91):
    driver = webdriver.Chrome()
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    try:

        # Mở trang
        driver.get(url)

        # Đợi  để trang tải
        time.sleep(1)

        # Lấy ra tất cả ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        #print(len(ul_tags))

        # Chọn thẻ ul thứ 21
        ul_painters = ul_tags[20]  # list start with index=0

        # Lấy tất cả các thẻ <li> thuộc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        # Tao danh sach cac url
        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
        for x in links:
            all_links.append(x)
    except:
        print("Error!")

    # Dong webdrive
    driver.quit()


######################################################
# III. Lay thong tin cua tung hoa si


def parse_date(date_text):
    # thử các định dạng khác nhau
    date_patterns = [
        r'[0-9]{1,2}\s+[A-Za-z]+\s+[0-9]{4}',# e.g., 15 March 1990
        r'[A-Za-z]+\s+[0-9]{1,2}\s+[0-9]{4}',# e.g., March 15, 1990 or March 15 1990
        r'[0-9]{4}' # Just the year
    ]

    for pattern in date_patterns:
        match = re.search(pattern, date_text)
        if match:
            return match.group()
    return ""

#lấy ra 3 người
for link in all_links:

    try:
        # Khoi tao webdriver
        driver = webdriver.Chrome()
        # Mo trang
        url = link
        driver.get(url)

        # Doi 2 giay
        time.sleep(0.5)

        # Lay ten hoa si
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""
        # Lay ngay sinh
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")

            birth = parse_date(birth_element.text)
        except:
            birth = ""
# Lay ngay mat
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = parse_date(death_element.text)


        except:
            death = ""
        # Lay nationality
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        # Tao dictionary thong tin cua hoa si
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

        # CHuyen doi dictionary thanh DataFrame
        painter_df = pd.DataFrame([painter])

        # Them thong tin vao DF chinh
        d = pd.concat([d, painter_df], ignore_index=True)

        # Dong web driver
        driver.quit()
    except:
        pass
####################
# IV. In thong tin
print(d)
file_name = 'Painters.xlsx'

# saving the Excel
d.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')