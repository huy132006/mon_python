# hoat dong 1
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Ví dụ Checkbutton")
cua_so.geometry("300x220")
cua_so.resizable(False, False)

tk.Label(cua_so, text="Chọn sở thích của bạn:", font=("Arial", 12)).pack(pady=10)

bien_doc_sach = tk.BooleanVar()
bien_the_thao = tk.BooleanVar()
bien_am_nhac = tk.BooleanVar()

tk.Checkbutton(cua_so, text="Đọc sách", variable=bien_doc_sach).pack(anchor="w", padx=30, pady=2)
tk.Checkbutton(cua_so, text="Thể thao", variable=bien_the_thao).pack(anchor="w", padx=30, pady=2)
tk.Checkbutton(cua_so, text="Âm nhạc", variable=bien_am_nhac).pack(anchor="w", padx=30, pady=2)

def xem_lua_chon():
    print("Đọc sách:", bien_doc_sach.get())
    print("Thể thao:", bien_the_thao.get())
    print("Âm nhạc:", bien_am_nhac.get())

tk.Button(cua_so, text="Xem lựa chọn (in ra console)", command=xem_lua_chon, bg="#4CAF50", fg="white").pack(pady=15)

cua_so.mainloop()
# hoạt động 2
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Ví dụ Radiobutton")
cua_so.geometry("300x200")
cua_so.resizable(False, False)

bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")  # Giá trị mặc định

tk.Label(cua_so, text="Chọn loại tài khoản:", font=("Arial", 12)).pack(pady=10)

tk.Radiobutton(cua_so, text="Cá nhân", variable=bien_loai_tai_khoan, value="ca_nhan").pack(anchor="w", padx=30, pady=2)
tk.Radiobutton(cua_so, text="Doanh nghiệp", variable=bien_loai_tai_khoan, value="doanh_nghiep").pack(anchor="w", padx=30, pady=2)

def xem_loai_tai_khoan():
    nhan_ket_qua.config(text=f"Bạn đã chọn: {bien_loai_tai_khoan.get()}")

tk.Button(cua_so, text="Xác nhận", command=xem_loai_tai_khoan, bg="#2196F3", fg="white").pack(pady=10)

nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 10, "bold"), fg="#333")
nhan_ket_qua.pack(pady=5)

cua_so.mainloop()