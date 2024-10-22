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

# #đường dẫn đến file thực thi geckodriver
# gecko_path = r"D:/selenium python/project2/geckodriver.exe"
#
# # khởi tạo đối tượng dịch vụ với dịch vụ geckodriver
# ser = Service(gecko_path)
#
# # tạo tùy chọn
# options = webdriver.firefox.options.Options()
# options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
#
# #thiết lập firefox chỉ hiển thị giao diện
# options.headless = False
#
# #khởi tạo driver
# driver = webdriver.Firefox(options=options, service=ser)
#

driver = webdriver.Chrome()

#tạo url
url = "https://gochek.vn/collections/all"

#truy cập
driver.get(url)

#tạm dừng 2s
time.sleep(2)

#tìm phần tử body của trang để gửi phím mũi tên xuống
body = driver.find_element(By.TAG_NAME, "body")
time.sleep(3)



# nhân phím mũi tên xuống nhiêù lần để cuộn từ từ
for i in range(50):
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)
#tạm dừng thêm 1s để tải trang hết nọi dung ở cuối trang
time.sleep(1)


# Tao cac list
stt = []
ten_san_pham = []
gia_ban = []
hinh_anh = []

# Tìm tất cả các
products= driver.find_elements(By.XPATH, "//div[contains(@class,'product-block')]")

# lay tung san pham
for i, product in enumerate(products, 1):


    # Lat ten sp
    try:
        tsp = product.find_element(By.TAG_NAME, 'h3').text
    except:
        tsp = ''

    # Lat gia sp
    try:
         # gsp = sp.find_element(By.CLASS_NAME, 'pro-price ').text
        gsp = product.find_element(By.XPATH, './/p[contains(@class, "pro-price")]//span[1]').text


    except:
       gsp = ''
    # Lat hinh anh
    try:
        ha = product.find_element(By.TAG_NAME, 'img').get_attribute('src')
    except:
        ha = ''

    # Chi them vao ds neu co ten sp
    #if (len(tsp) > 0) and (tsp not in ten_san_pham or gsp):
    if (len(tsp) > 0):

        ten_san_pham.append(tsp)
        gia_ban.append(gsp)
        hinh_anh.append(ha)
# Tạo df
df = pd.DataFrame({
    "Tên sản phẩm": ten_san_pham,
    "Giá bán": gia_ban,
    "Hình ảnh": hinh_anh

})

df.to_excel('spgochek.xlsx', index=False)
driver.quit()