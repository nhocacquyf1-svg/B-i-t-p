#B1
tong = 0
for i in range (3):
    diem =float (input("Nhập điểm của bạn: "))
    tong += diem
diem_tb = tong/3
print ("Điểm trung bình là:", diem_tb)

#B2
ho_ten =  (input("Nhập họ và tên: "))
ma_sv =  (input("Nhập mã sinh viên: "))
nam_sinh = int (input("Nhập năm sinh: "))
tuoi = 2026 - nam_sinh
print (f"Họ và tên: {ho_ten}, Mã sinh viên: {ma_sv}, Tuổi: {tuoi}")