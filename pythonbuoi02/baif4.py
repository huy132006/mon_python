# bài 4.1
cau = "Lap trinh Python rat thu vi"
print(cau[0]) 
print(cau[-1]) 
print(cau[4:10]) 
print(cau[:8]) 
print(cau[11:]) 
print(cau[::-1]) 
# bài 4.2
ten = "Nam"
ten_moi = "T" + ten[1:]
print(ten_moi)
# bài 4.3
cau = " Toi dang HOC Python rat vui "
print(cau.strip()) 
print(cau.strip().upper())
print(cau.strip().lower()) 
print(cau.strip().replace("HOC", "hoc"))
print(cau.strip().split()) 
print(len(cau.strip().split())) 
print(cau.count("o")) 
print(cau.find("Python")) 
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))
# bài 4.4
ho_ten_tho = " nguyen van an "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach) # Nguyen Van An