import numpy as np


diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)

print(f"Kiểu dữ liệu: List = {type(diem_list)} | NumPy Array = {type(diem_array)}")


diem_cong_them = diem_array + 0.5
print("\nMảng điểm sau khi cộng 0.5 (Dùng NumPy):", diem_cong_them)


diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("Mảng điểm sau khi cộng 0.5 (Dùng List thuần):", diem_cong_them_list)


print("\n--- THỐNG KÊ ĐIỂM ---")
print(f"Điểm trung bình (Mean) : {np.mean(diem_array):.2f}")
print(f"Điểm cao nhất (Max)     : {np.max(diem_array)}")
print(f"Điểm thấp nhất (Min)    : {np.min(diem_array)}")
print(f"Độ lệch chuẩn (Std)     : {np.std(diem_array):.2f}")


print("\n--- THAO TÁC MA TRẬN 2 CHIỀU ---")
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma trận ban đầu:\n", ma_tran)
print("Kích thước ma trận (shape):", ma_tran.shape)
print("Ma trận sau khi nhân đôi (ma_tran * 2):\n", ma_tran * 2)