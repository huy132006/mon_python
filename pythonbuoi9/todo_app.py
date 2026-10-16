import tkinter as tk
from tkinter import messagebox

danh_sach_cong_viec = []  # List lưu trữ các tuple: (noi_dung, da_hoan_thanh)

def lam_moi_listbox():
    listbox_cong_viec.delete(0, tk.END)
    for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
        tien_to = "[Đã xong] " if da_hoan_thanh else "[Chưa xong] "
        listbox_cong_viec.insert(tk.END, tien_to + noi_dung)

def them_cong_viec():
    noi_dung = bien_cong_viec_moi.get().strip()
    if not noi_dung:
        messagebox.showerror("Lỗi", "Vui lòng nhập nội dung công việc trước khi thêm.")
        return
    danh_sach_cong_viec.append((noi_dung, False))
    bien_cong_viec_moi.set("")
    lam_moi_listbox()

def xoa_cong_viec():
    lua_chon = listbox_cong_viec.curselection()
    if not lua_chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn một công việc trong danh sách để xóa.")
        return
    vi_tri = lua_chon[0]
    danh_sach_cong_viec.pop(vi_tri)
    lam_moi_listbox()

def danh_dau_hoan_thanh():
    lua_chon = listbox_cong_viec.curselection()
    if not lua_chon:
        messagebox.showerror("Lỗi", "Vui lòng chọn một công việc để đánh dấu hoàn thành.")
        return
    vi_tri = lua_chon[0]
    noi_dung, _ = danh_sach_cong_viec[vi_tri]
    danh_sach_cong_viec[vi_tri] = (noi_dung, True)
    lam_moi_listbox()

cua_so = tk.Tk()
cua_so.title("Ứng dụng Ghi chú công việc")
cua_so.geometry("450x420")
cua_so.resizable(False, False)

bien_cong_viec_moi = tk.StringVar()

tk.Label(cua_so, text="TO-DO LIST", font=("Arial", 16, "bold"), fg="#333").grid(
    row=0, column=0, columnspan=3, pady=15
)

entry_cong_viec = tk.Entry(cua_so, textvariable=bien_cong_viec_moi, width=30, font=("Arial", 11))
entry_cong_viec.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="we")

tk.Button(cua_so, text="Thêm", command=them_cong_viec, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).grid(
    row=1, column=2, padx=10, pady=5
)

listbox_cong_viec = tk.Listbox(cua_so, width=50, height=14, font=("Arial", 10))
listbox_cong_viec.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

tk.Button(cua_so, text="Đánh dấu hoàn thành", command=danh_dau_hoan_thanh, bg="#2196F3", fg="white", font=("Arial", 10)).grid(
    row=3, column=0, padx=10, pady=10, sticky="ew"
)

tk.Button(cua_so, text="Xóa công việc", command=xoa_cong_viec, bg="#F44336", fg="white", font=("Arial", 10)).grid(
    row=3, column=1, padx=10, pady=10, sticky="ew"
)

if __name__ == "__main__":
    cua_so.mainloop()