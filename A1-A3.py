#A1
ten = "thien"
tuoi =10
diem_tb = 5.3
da_tot_nghiep = True
print (type(ten))
print (type(tuoi))
print (type(diem_tb))
print (type(da_tot_nghiep))

#A2
chieu_dai = float (input("Nhập chiều dài: "))
chieu_rong = float (input("Nhập chiều rộng: "))
p = (chieu_dai + chieu_rong) * 2
s = chieu_dai * chieu_rong
print("Chu vi của hình chữ nhật là:", p)
print("Diện tích của hình chữ nhật là:", s)

#A3
cao = float (input("nhập chiều cao của bạn theo m: "))
nang = float (input("nhập cân nặng của bạn theo kg: "))
BMI = nang/cao**2
print("Chỉ số BMI của bạn là:", round(BMI,2))

#A4
giay = int (input("Nhập số giây: "))
gio = giay // 3600
phut = (giay % 3600) //60
giay_con_lai = giay % 60
print(f"Thời gian tương ứng là: {gio} giờ {phut} phút {giay_con_lai} giây")
