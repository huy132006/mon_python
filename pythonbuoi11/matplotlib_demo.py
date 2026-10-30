import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("diem_sinh_vien.csv")


diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

plt.figure(figsize=(6, 4))
plt.bar(diem_trung_binh_mon.index, diem_trung_binh_mon.values, color="skyblue")
plt.title("Điểm trung bình theo môn học")
plt.xlabel("Môn học")
plt.ylabel("Điểm trung bình")
plt.ylim(0, 10)
plt.savefig("bieu_do_cot.png")
print("Đã lưu biểu đồ cột thành công tại: bieu_do_cot.png")
plt.show()

# Bài tập 3.2 – Biểu đồ đường: Xu hướng điểm qua các lần kiểm tra
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

plt.figure(figsize=(6, 4))
plt.plot(lan_kiem_tra, diem_qua_cac_lan, marker="o", color="green", linestyle="-", linewidth=2)
plt.title("Xu hướng điểm qua các lần kiểm tra")
plt.xlabel("Lần kiểm tra")
plt.ylabel("Điểm số")
plt.ylim(0, 10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig("bieu_do_duong.png")
print("Đã lưu biểu đồ đường thành công tại: bieu_do_duong.png")
plt.show()