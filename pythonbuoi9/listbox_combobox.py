# bài 3.1 
import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Ví dụ Listbox")
cua_so.geometry("300x250")
cua_so.resizable(False, False)

tk.Label(cua_so, text="Chọn môn học:", font=("Arial", 11)).pack(pady=5)

listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single", height=5, font=("Arial", 10))
for mon in ["Toán", "Lý", "Hóa", "Văn", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)
listbox_mon_hoc.pack(pady=5)

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        nhan_ket_qua.config(text=f"Môn đã chọn: {listbox_mon_hoc.get(lua_chon[0])}")
    else:
        nhan_ket_qua.config(text="Vui lòng chọn một môn học!")

tk.Button(cua_so, text="Xem môn đã chọn", command=xem_mon_da_chon, bg="#FF9800", fg="white").pack(pady=5)

nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 10, "bold"))
nhan_ket_qua.pack(pady=5)

cua_so.mainloop()
# bài 3.2
import tkinter as tk
from tkinter import ttk

cua_so = tk.Tk()
cua_so.title("Ví dụ Combobox")
cua_so.geometry("300x180")
cua_so.resizable(False, False)

tk.Label(cua_so, text="Chọn thành phố:", font=("Arial", 11)).pack(pady=10)

combobox_thanh_pho = ttk.Combobox(cua_so, values=["Hà Nội", "Đà Nẵng", "TP.HCM", "Huế"], font=("Arial", 10))
combobox_thanh_pho.current(0)  # Chọn giá trị đầu tiên làm mặc định
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    nhan_ket_qua.config(text=f"Bạn chọn: {combobox_thanh_pho.get()}")

tk.Button(cua_so, text="Xác nhận", command=xem_thanh_pho, bg="#9C27B0", fg="white").pack(pady=10)

nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 10, "bold"))
nhan_ket_qua.pack()

cua_so.mainloop()