from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
import time
import pandas as pd

#đường dẫn đến file thực thi geckodriver
gecko_path = r"D:/selenium python/project2/geckodriver.exe"

# khởi tạo đối tượng dịch vụ với dịch vụ geckodriver
ser = Service(gecko_path)

# tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"

#thiết lập firefox chỉ hiển thị giao diện
options.headless = False

#khởi tạo driver
driver = webdriver.Firefox(options=options, service=ser)

#tạo url
url = "https://pythonscraping.com/pages/files/form.html"

#truy cập
driver.get(url)

#tạm dừng 2s
time.sleep(2)
#tìm thẻ để nhập
firstname_input = driver.find_element(By.XPATH, "//input[@name = 'firstname']")
lastname_input = driver.find_element(By.XPATH, "//input[@name = 'lastname']")
# send_keys gửi những thông số để đăng nhap
firstname_input.send_keys('Le van')
lastname_input.send_keys('Tran')
time.sleep(2)
#nhan nut
button = driver.find_element(By.XPATH, "//input[@type = 'submit']")
button.click()
time.sleep(5)

driver.quit()