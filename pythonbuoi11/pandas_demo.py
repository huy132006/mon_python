import pandas as pd

# 0. Tạo nội dung file CSV mẫu nếu chưa có trên máy
csv_data = """ho_ten,mon_hoc,diem
Nguyen Van A,Toan,8.5
Tran Thi B,Toan,6.0
Le Van C,Toan,9.0
Pham Thi D,Toan,4.5
Nguyen Van A,Ly,7.5
Tran Thi B,Ly,5.5
Le Van C,Ly,8.0
Pham Thi D,Ly,6.5
Nguyen Van A,Hoa,9.0
Tran Thi B,Hoa,6.5
Le Van C,Hoa,8.5
Pham Thi D,Hoa,5.0"""

with open("diem_sinh_vien.csv", "w", encoding="utf-8") as f:
    f.write(csv_data)

# Bài tập 2.1 – Đọc CSV & xem tổng quan
df = pd.read_csv("diem_sinh_vien.csv")
print("=== BÀI TẬP 2.1: TỔNG QUAN DỮ LIỆU ===")
print("5 dòng đầu tiên:")
print(df.head())
print("Kích thước (Số dòng, Số cột):", df.shape)
print("Danh sách tên cột:", df.columns.tolist())

# Bài tập 2.2 – Thống kê theo môn học
print("\n=== BÀI TẬP 2.2: THỐNG KÊ THEO MÔN HỌC ===")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print("Điểm trung bình theo từng môn:\n", diem_trung_binh_mon)
print(f"Điểm trung bình toàn bộ: {df['diem'].mean():.2f}")
print(f"Điểm cao nhất: {df['diem'].max()}")
print(f"Điểm thấp nhất: {df['diem'].min()}")

# Bài tập 2.3 – Tính DTB từng sinh viên & lọc đạt/không đạt
print("\n=== BÀI TẬP 2.3: ĐIỂM TB SINH VIÊN VÀ LỌC ĐẠT/KHÔNG ĐẠT ===")
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print("Điểm trung bình của từng sinh viên:\n", diem_tb_sv)

sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nDanh sách sinh viên đạt (>= 5.0):")
print(sinh_vien_dat if not sinh_vien_dat.empty else "Không có")

print("\nDanh sách sinh viên không đạt (< 5.0):")
print(sinh_vien_khong_dat if not sinh_vien_khong_dat.empty else "Không có")