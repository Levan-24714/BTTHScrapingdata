#import
from pymongo import MongoClient
from datetime import datetime

#buoc 1: ket noi den mongodb
client = MongoClient("mongodb://localhost:27017/")
client.drop_database('Facebookdata1')
db = client['Facebookdata1']  # chon csdl Facebookdata1

#buoc 2: tao cac collection
users_collection = db['users']
posts_collection = db['posts']
comment_collection = db['comment']
#buoc 3: them du lieu nguoi dung
users_data = [
    {'user_id': 1, 'name': "Nguyen Van A", 'email': "a@gmail.com", 'age': 25},
    {'user_id': 2, 'name': "Tran Thi B", 'email': "b@gmail.com", 'age': 30},
    {'user_id': 3, 'name': "Le Van C", 'email': "c@gmail.com", 'age': 22}
]
users_collection.insert_many(users_data)

# buoc 4:them du lieu  binh luan
posts_data =[
    {'post_id': 1, 'user_id': 1, 'content': "Hôm nay thật đẹp trời!", 'created_at': datetime(2024, 10, 1)},
    {'post_id': 2, 'user_id': 2, 'content': "Mình vừa xem một bộ phim hay!", 'created_at': datetime(2024, 10, 2)},
    {'post_id': 3, 'user_id': 1, 'content': "Chúc mọi người một ngày tốt lành!", 'created_at': datetime(2024, 10, 3)}
]
posts_collection.insert_many(posts_data)

#buoc 5: them du lieu binh luan
comment_data = [
    {'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': datetime(2024, 10, 1)},
    {'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': datetime(2024, 10, 2)},
    {'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': datetime(2024, 10, 3)}
]
comment_collection.insert_many(comment_data)

#buoc 6: truy xuat du lieu
##1
print("Tất cả người dùng")
for user in users_collection.find():
    print(user)

##2
print("Tất cả bài đăng của người dung với user_id = 1 :")
for post in posts_collection.find({'user_id': 1}):
    print(post)

##3
print('Xem tất cả các bài bình luận với post_id = 1 :')
for comment in comment_collection.find({'post_id': 1}):
    print(comment)


##4
print("Người dùng có độ tuổi trên 25 :")
user_age = users_collection.find({'age': {"$gt": 25}})
for user in user_age:
    print(user)

##5
start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 11, 1)
print("Tất cả bài đăng được tạo trong tháng 10")
creat_10 = posts_collection.find({"created_at": {"$gte": start_date, "$lt": end_date}})
for post10 in creat_10:
    print(post10)

##6 Cập nhật nội dung bài đăng của người dùng với post_id = 1
posts_collection.update_one({'post_id': 1}, {'$set': {'content': "Hôm nay thời tiết thật đẹp!" }})

##7 Xóa bình luận với comment_id = 2
comment_collection.delete_one({'comment_id': 2})

print("\nDữ liệu người dùng sau khi cập nhật:")
for users in posts_collection.find():
    print(users)

print("\nDữ liệu người dùng sau khi  xóa tệp:")
for users in comment_collection.find():
    print(users)



client.close()