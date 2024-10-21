#import
from pymongo import MongoClient
from datetime import datetime

#buoc 1: ket noi den mongodb
client = MongoClient("mongodb://localhost:27017/")
client.drop_database('driveManagement1')
db = client['driveManagement1']  # chon csdl Facebookdata1

#buoc 2: tao cac collection
files_collection = db['files']

#buoc 3: them dữ liệu
files_data = [
    {'file_id': 1, 'name': "Report.pdf", 'size': 2048, 'owner': "Nguyen Van A", 'created_at': datetime(2024, 1, 10), 'shared': False},
    {'file_id': 2, 'name': "Presentation.pptx", 'size': 5120, 'owner': "Tran Thi B", 'created_at': datetime(2024, 1, 15), 'shared': True},
    {'file_id': 3, 'name': "Image.png", 'size': 1024, 'owner': "Le Van C", 'created_at': datetime(2024, 1, 20), 'shared': False},
    {'file_id': 4, 'name': "Spreadsheet.xlsx", 'size': 3072, 'owner': "Pham Van D", 'created_at': datetime(2024, 1, 25), 'shared': True},
    {'file_id': 5, 'name': "Notes.txt", 'size': 512, 'owner': "Nguyen Thi E", 'created_at': datetime(2024, 1, 30), 'shared': False}
]
files_collection.insert_many(files_data)

##1Xem tất cả tệp trong bộ sưu tập 'files'
print("Tất cả người dùng")
for file in files_collection.find():
    print(file)

##2 Tìm tệp có kích thước lớn hơn 2000KB
print("tệp có kích thước lớn hơn 2000KB :")
size2000 = files_collection.find({'size': {"$gt": 2000}})
for user in size2000:
    print(user)

##3Đếm tổng số tệp
print('Tổng số tệp:', files_collection.count_documents({}))

##4 Tìm tất cả tệp được chia sẻ
print("tất cả tệp được chia sẻ")
for shared_file in files_collection.find({'shared': True}):
    print(shared_file)

##5 Thống kê số lượng tệp theo chủ sở hữu
print("Thống kê số lượng tệp theo chủ sở hữu:")
statistics = files_collection.aggregate([{'$group': { "_id": "$owner", "count": {"$sum": 1}}}])
for statistic in statistics:
    print(statistic)


### cập nhập và xóa thông tin tệp
##6 cập nhập trạng thái chia sẻ của tệp với file_id = 1 thành True
#print('Cập nhập trạng thái chia sẻ của tệp với file_id = 1 thành True: ')
files_collection.update_one({'file_id': 1}, {'$set': {'shared': True}})

##7  Xóa tệp với file_id = 3
#print(' Xóa tệp với file_id = 3')
files_collection.delete_one({'file_id': 3})


##câu hỏi 1:Tìm tất cả tệp của người dùng có tên là "Nguyen Van A"
print("tất cả tệp của người dùng có tên là 'Nguyen Van A'")
for people in files_collection.find({'owner': 'Nguyen Van A'}):
    print(people)

##câu 2: Tìm tệp lớn nhất trong bộ sưu tập.
print(' Tệp lớn nhất trong bộ sưu tập:')
for size_max in files_collection.find().sort({'size': -1}).limit(1):
    print(size_max)

## câu 3:Tìm số lượng tệp có kích thước nhỏ hơn 1000KB
print(' Tìm số lượng tệp có kích thước nhỏ hơn 1000KB')
for amount in files_collection.find({'size': {'$lt': 1000}}):
    print(amount)

##câu 4: Tìm tất cả tệp được tạo trong tháng 1 năm 2024.
print(' Tất cả tệp được tạo trong tháng 1 năm 2024:')
for day in files_collection.find({'created_at': {'$gte': datetime(2024, 1, 1), '$lt': datetime(2024, 2, 1)}}):
    print(day)

##câu 5:Cập nhật tên tệp với `file_id` là 4 thành "New Spreadsheet.xlsx".
files_collection.update_one({'file_id': 4}, {'$set': {'name': 'New Spreadsheet.xlsx'}})

##Câu 6:Xóa tất cả tệp có kích thước nhỏ hơn 1000KB.
files_collection.delete_one({'size': {'$lt': 1000}})
print("\nDữ liệu người dùng sau khi cập nhập, xóa tệp:")
for users in files_collection.find():
    print(users)

client.close()