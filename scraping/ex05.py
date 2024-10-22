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
import getpass
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
url = "https://www.reddit.com/login/"

#truy cập
driver.get(url)

#nhap thong ti nguoi dung
my_email = input('Please provide your email: ')
my_password = getpass.getpass('Please provide your password:')


#đăng nhập
username_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")

#nhấn thông tin và nhấn nút enter
username_input.send_keys(my_email)
password_input.send_keys(my_password + Keys.ENTER)
time.sleep(5)


#button_login = driver.find_element(By.XPATH, "//button[text()='login]")
#button_login.click()
driver.quit()


