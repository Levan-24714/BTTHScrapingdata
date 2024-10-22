from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
#Đườn dẫn đến file thực thi geckodriver
gecko_path = "D:/selenium python/project2/geckodriver.exe"

#khởi tạo đối tượng dịch vụ vs đường grckodriver
ser = Service(gecko_path)

# tao tuy chon

options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"


# thiet lap firefox chi hien thi giao dien
options.headless = False


#khoi tao driver
driver = webdriver.Firefox(options=options, service=ser)

#taoj url
url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

#truy cap
driver.get(url)

#in ra noi dung cua trang wed
print("Before:=========================")
print(driver.page_source)

#tam dung khoang 3 s
time.sleep(3)


# in lai
print("\n\n\nAfter: ============================= ")
print(driver.page_source)
#dong browser
driver.quit()