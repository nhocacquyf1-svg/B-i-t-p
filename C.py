#C1
so = int (input("Nhập số nguyên:" ))
if so % 2==0:
    print ("Đây là số chắn")
else:
    print ("Đây là số lẻ")

#C2
so1 = float(input("Nhập số thứ nhất:" ))
so2 = float(input("Nhập số thứ hai:" ))
if so1 >so2:
    print ("Số lớn hơn là: ",so1)
elif so1<so2:
    print ("Số lớn hơn là: ",so2)
else:
    print ("Hai số bằng nhau")

#C3
diem_tb = float(input("Nhập điểm trung bình: "))
while diem_tb < 0 or diem_tb > 10:
    diem_tb = float(input("Điểm không hợp lệ, vui lòng nhập lại: "))
if diem_tb >= 8.5:
    print ("Học sinh giỏi")
elif diem_tb >= 7:   
    print ("Học sinh khá")  
elif diem_tb >= 5:
    print ("Học sinh trung bình")
else:
    print ("Học sinh yếu")

#C4
nam = int(input("Nhập năm: "))
if nam % 400 ==0:
    print ("Đây là năm nhuận")
else:
    print ("Đây không phải là năm nhuận")