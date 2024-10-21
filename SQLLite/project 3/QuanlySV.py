from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("600x800")
#
# #Ket noi toi db
# conn = sqlite3.connect('address_qlsv.db')
# c =conn.cursor()
#
# #tao cang de luu tru
# c.execute('''
#       CREATE TABLE QLSV(
#         idstudent  integer primary key,
#         first_name   text,
#         last_name    text,
#         id_class     integer,
#         year         text,
#         AVG          Float
#       )
# ''')

def them():

    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('address_qlsv.db')
    c = conn.cursor()
    # Lấy dữ liệu đã nhập
    idstudent_value = idstudent.get()
    fisrtNname_value = f_name.get().lower()
    lastName_value = l_name.get().lower()
    IdClass_value = id_class.get().lower()
    Year_value = year.get()
    avg_value = AVG.get()

    # kiểm tra nếu ô nào để trống
    if not idstudent_value or not fisrtNname_value or not lastName_value or not avg_value:
        messagebox.showerror("Thông báo", "Vui lòng nhập đầy đủ thông tin")
        return #dừng lại nếu thiếu thông tin
    # avg_value = float(avg_value)
    try:
        avg_value = float(avg_value)
        if not (0 <= avg_value <= 10):
            messagebox.showerror("Thông báo", "Điểm trung bình phải nằm trong khoảng từ 0 đến 10.")
            return  # Dừng lại nếu điểm không hợp lệ
    except ValueError:
        messagebox.showerror("Thông báo", "Vui lòng nhập số hợp lệ cho điểm trung bình.")
        return  # Dừng lại nếu không phải số


    #kiểm tra xem thông tin đã tồn tại trong cơ sở dữ liẹu chưa(so sánh không phân biệt chữ hoa chữ thường)

    c.execute("SELECT * FROM QLSV WHERE idstudent=:idstudent", {'idstudent': idstudent_value})
    existing_record = c.fetchone()
    if existing_record:
        messagebox.showerror("Thông báo!", "Mã sinh viên đã tồn tại.")
    else:
        # Thực hiện câu lệnh để thêm
        c.execute('''
                        INSERT INTO
                        QLSV (idstudent, first_name, last_name, id_class, year, AVG)
                        VALUES
                        (:idstudent, :first_name, :last_name, :id_class, :year, :AVG)
                    ''', {
            'idstudent': idstudent_value,
            'first_name': fisrtNname_value,
            'last_name': lastName_value,
            'id_class': IdClass_value,
            'year': Year_value,
            'AVG': avg_value
        })
        conn.commit()
        messagebox.showinfo("Thông báo", "Thêm thành công!")

    conn.close()

    # Reset form
    idstudent.delete(0, END)
    f_name.delete(0, END)
    l_name.delete(0, END)
    id_class.delete(0, END)
    year.delete(0, END)
    AVG.delete(0, END)


    # Hien thi lai du lieu
    truy_van()
    print("")

def xoa():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('address_qlsv.db')
    c = conn.cursor()
    c.execute("""
               Select *
               From QLSV
               Where idstudent = :idstudent
               """, {
        'idstudent': delete_box.get()
    })
    # Lay 1 dong du lieu ra
    records = c.fetchone()

    if records is None:
        messagebox.showwarning("Thong bao", "Id khong ton tai")
        delete_box.delete(0, END)
    else:
        c.execute('''DELETE FROM QLSV 
                                  WHERE idstudent=:idstudent''',
                  {'idstudent': delete_box.get()})
        delete_box.delete(0, END)

        conn.commit()
        messagebox.showinfo("Thông báo", "Đã xóa!")
    conn.close()
    # Hiên thi thong bao

    # Hiển thị lại dữ liệu
    truy_van()
def truy_van():
    # Xóa đi các dữ liệu trong TreeView
    for row in tree.get_children():
        tree.delete(row)

    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('address_qlsv.db')
    c = conn.cursor()
    c.execute("SELECT * FROM QLSV")
    records = c.fetchall()

    # Hien thi du lieu
    for r in records:
        tree.insert("", END, values=(r[0], r[1], r[2], r[3], r[4], r[5]))

    # Ngat ket noi
    conn.close()
    print("")

def chinh_sua():
    conn = sqlite3.connect('address_qlsv.db')
    c = conn.cursor()
    c.execute("""
                  Select *
                  From QLSV
                  Where idstudent = :idstudent
                  """, {
        'idstudent': delete_box.get()
    })
    # Lay 1 dong du lieu ra
    records = c.fetchone()


    if records is None:
        messagebox.showwarning("Thong bao", "Id khong ton tai")
        delete_box.delete(0, END)
    else:
        global editor
        editor = Tk()
        editor.title('Cập nhật bản ghi')
        editor.geometry("400x300")
        conn = sqlite3.connect('address_qlsv.db')
        c = conn.cursor()
        record_id = delete_box.get()
        c.execute("SELECT * FROM QLSV WHERE idstudent=:idstudent", {'idstudent': record_id})
        records = c.fetchall()
        global f_id_editor, f_name_editor, l_name_editor,id_class_editor, year_editor, AVG_editor

        #f_id_editor = Entry(editor, width=30)
        #f_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=1, column=1, padx=20)
        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=2, column=1)
        id_class_editor = Entry(editor, width=30)
        id_class_editor.grid(row=3, column=1)
        year_editor = Entry(editor, width=30)
        year_editor.grid(row=4, column=1)
        AVG_editor = Entry(editor, width=30)
        AVG_editor.grid(row=5, column=1)


        #f_id_label = Label(editor, text="Mã số sinh viên")
        # f_id_label.grid(row=0, column=0, pady=(10, 0))
        f_name_label = Label(editor, text="Họ")
        f_name_label.grid(row=1, column=0)
        l_name_label = Label(editor, text="Tên")
        l_name_label.grid(row=2, column=0)
        id_class_label = Label(editor, text="Mã lớp")
        id_class_label.grid(row=3, column=0)
        year_label = Label(editor, text="Năm nhập học")
        year_label.grid(row=4, column=0)
        AVG_label = Label(editor, text="Điểm trung bình")
        AVG_label.grid(row=5, column=0)


        for record in records:
            #f_id_editor.insert(0, record[0])
            f_name_editor.insert(0, record[1])
            l_name_editor.insert(0, record[2])
            id_class_editor.insert(0, record[3])
            year_editor.insert(0, record[4])
            AVG_editor.insert(0, record[5])

        edit_btn = Button(editor, text="Lưu bản ghi", command=cap_nhap)
        edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)



def cap_nhap():
    conn = sqlite3.connect('address_qlsv.db')
    c = conn.cursor()
    record_id = delete_box.get()  # Lấy ID từ hộp "delete_box", không cho phép chỉnh sửa
    avg_value = AVG_editor.get()
    try:
        avg_value = float(avg_value)
        if not (0 <= avg_value <= 10):
            messagebox.showerror("Thông báo", "Điểm trung bình phải nằm trong khoảng từ 0 đến 10.")
            return  # Dừng lại nếu điểm không hợp lệ
    except ValueError:
        messagebox.showerror("Thông báo", "Vui lòng nhập số hợp lệ cho điểm trung bình.")
        return  # Dừng lại nếu không phải số

    # Cập nhật các trường khác
    c.execute("""UPDATE QLSV SET
                   first_name = :first,
                   last_name = :last,
                   id_class = :id_class,
                   year = :year,
                   AVG = :AVG
                   WHERE idstudent = :idstudent""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'id_class': id_class_editor.get(),
                  'year': year_editor.get(),
                  'AVG': AVG_editor.get(),
                  'idstudent': record_id  # Sử dụng ID để tìm bản ghi

              })

    conn.commit()
    conn.close()
    editor.destroy()

#khung o nhap lieu
input_frame = Frame(root)
input_frame.pack(pady=10)

# cac o nhap lieu cho cua so chinh
idstudent = Entry(input_frame, width=30)
idstudent.grid(row=0, column=1, padx=20, pady=(10, 0))
f_name = Entry(input_frame, width=30)
f_name.grid(row=1, column=1)
l_name = Entry(input_frame, width=30)
l_name.grid(row=2, column=1)
id_class = Entry(input_frame, width=30)
id_class.grid(row=3, column=1)
year = Entry(input_frame, width=30)
year.grid(row=4, column=1)
AVG = Entry(input_frame, width=30)
AVG.grid(row=5, column=1)


# Các nhãn
id_label = Label(input_frame, text="Mã sinh viên")
id_label.grid(row=0, column=0, pady=(10, 0))
f_name_label = Label(input_frame, text="Họ")
f_name_label.grid(row=1, column=0)
l_name_label = Label(input_frame, text="Tên")
l_name_label.grid(row=2, column=0)
id_class_label = Label(input_frame, text="Mã lớp")
id_class_label.grid(row=3, column=0)
year_label = Label(input_frame, text="Năm nhập học")
year_label.grid(row=4, column=0)
AVG_label = Label(input_frame, text="Điểm trung bình")
AVG_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm bản ghi", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị bản ghi", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
delete_box_label = Label(button_frame, text="Chọn MSSV để xóa")
delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa bản ghi", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("Mã sinh viên", "Họ", "Tên", "Mã lớp", "Năm nhập học", "Điểm trung bình")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
tree.pack()


# Định nghĩa tiêu đề cho các cột
for col in columns:
    tree.heading(col, text=col)

# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
truy_van()
root.mainloop()