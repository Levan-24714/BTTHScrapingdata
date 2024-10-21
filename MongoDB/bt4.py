#import
from pymongo import MongoClient
from datetime import datetime

#buoc 1: ket noi den mongodb
client = MongoClient("mongodb://localhost:27017/")
client.drop_database('tiktokABC')
db = client['tiktokABC']  # chon csdl tiktok

#buoc 2: tapj cacs collection
users_collection = db['users']
videos_collection = db['videos']

#buoc 3 :
users_data = [
    {'user_id': 1, 'username': "user1", 'full_name': "Nguyen Van A", 'followers': 1500, 'following': 200 },
    {'user_id': 2, 'username': "user2", 'full_name': "Tran Thi B", 'followers': 2000, 'following': 300 },
    {'user_id': 3, 'username': "user3", 'full_name': "Le Van C", 'followers': 500, 'following': 100 }
]
users_collection.insert_many(users_data)

#buoc 4: them du lieu ve video
videos_data =[
{ 'video_id': 1, 'user_id': 1, 'title': "Video 1", 'views': 10000, 'likes': 500, 'created_at': datetime(2024, 1, 1)},
    { 'video_id': 2, 'user_id': 2, 'title': "Video 2", 'views': 20000, 'ikes': 1500, 'created_at': datetime(2024, 1, 5)},
    { 'video_id': 3, 'user_id': 3, 'title': "Video 3", 'views': 5000, 'likes': 200, 'created_at': datetime(2024, 1, 10)}
]
videos_collection.insert_many(videos_data) # them du lieu vao video

#buoc 5: truy xuat du lieu
#5.1 xem tat ca nguoi dung
print("tat ca nguoi dung")
for user in users_collection.find():
    print(user)


#5.2 tim video co nhieu nguoi xem nhat
print('video co nhieu luot xem nhat: ')
mosted_viewed_video = videos_collection.find().sort('views', -1).limit(1)
for user in mosted_viewed_video:
    print(user)

#5.3 timf tat ca video cua nguoi dung co username la "user1"
print("\nTat ca video cua nguoi dung 'user1 ' :")
user_videos = videos_collection.find({'user_id': 1})
for video in user_videos:
    print(video)

# Bước 6: Cập nhật dữ liệu
# Cập nhật số người theo dõi của người dùng với `user_id` là 1 lên 2000
users_collection.update_one({'user_id': 1}, {'$set': {'followers': 2000}})

# Bước 7: Xóa video có `video_id` là 3
videos_collection.delete_one({'video_id': 3})

# Bước 8: Xem lại dữ liệu sau khi cập nhật và xóa
print("\nDữ liệu người dùng sau khi cập nhật:")
for user in users_collection.find():
    print(user)

print("\nDữ liệu video sau khi xóa:")
for video in videos_collection.find():
    print(video)

# Đóng kết nối
client.close()

