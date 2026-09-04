# baif 5.1
a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
# baif 5.2
diem = 6.5
tuoi = 20
la_loai_kha = (diem >= 6.5) and (diem < 8.0)
print("Điểm đạt loại Khá:", la_loai_kha)
ngoai_do_tuoi_lao_dong = (tuoi < 18) or (tuoi > 60)
print("Chưa đủ 18 hoặc trên 60:", ngoai_do_tuoi_lao_dong)
print("Phủ định điều kiện điểm Khá:", not la_loai_kha)
print("Phủ định điều kiện độ tuổi:", not ngoai_do_tuoi_lao_dong)
# bai 5.3
x = 10
x += 5
print("x += 5:", x)
x -= 5
print("x  -= 5:", x)
x *= 5
print("x  *= 5:", x)
x /= 5
print("x  /= 5:", x)
x //= 5
print("x  //= 5:", x)
x **= 5
print("x  **= 5:", x)
danh_sach = [1, 2, 3, "python"]
print("3 trong danh_sach:", 3 in danh_sach)
ds1 = [1, 2, 3]
ds2 = ds1
print("ds1 is ds2:", ds1 is ds2)
# bai 5.4
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)