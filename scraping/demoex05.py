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

# Đăng nhập
#username_input =driver.find_element(By.XPATH, "//input[@name='username']")
#password_input =driver.find_element(By.XPATH, "//input[@name='password']")

# Nhấn thông tin và nhấn nút Enter
#username_input.send_keys(my_email)
#password_input.send_keys(my_password + Keys.ENTER)
#time.sleep(5)

actionChains = ActionChains(driver)
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.send_keys(my_email).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys(my_password+Keys.ENTER).perform()

#button_login = driver.find_element(By.XPATH,"//button[text()='Log in']")
#button_login.click()

time.sleep(10)

# Truy cap trang post bai
url2 = 'https://www.reddit.com/user/Hungry_Revenue_8235/submit/?type=TEXT'
driver.get(url2)
time.sleep(2)

for i in range(20):
   actionChains.key_down(Keys.TAB).perform()
   time.sleep(1)

actionChains.send_keys('Vi du post').perform()

actionChains.key_down(Keys.TAB).perform()
actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys('Tran Le Van' + Keys.ENTER).perform()

for i in range(2):
      actionChains.key_down(Keys.TAB).perform()
      time.sleep(3)

actionChains.key_down(Keys.Enter).perform()

time.sleep(100)
driver.quit()