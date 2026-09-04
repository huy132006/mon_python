# bai 6.1
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))
# bai 6.2
ho_ten = "pham thanh binh"
diem_toan = 9.0
diem_ly = 6.5
diem_hoa = 8.0
dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi :", la_gioi)
print("Dat loai Kha :", la_kha)

print("Dat loai Trung binh:", la_trung_binh)
print("Dat loai Yeu :", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))