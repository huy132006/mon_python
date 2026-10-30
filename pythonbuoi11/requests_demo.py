import requests

# Bài tập 5.1 - Gọi API GitHub (Thông tin repo CPython)
print("=== BÀI TẬP 5.1: GỌI GITHUB API ===")
url_github = "https://api.github.com/repos/python/cpython"
response = requests.get(url_github)

if response.status_code == 200:
    du_lieu = response.json()
    print("Tên repository:", du_lieu.get("full_name"))
    print("Số lượt gắn sao (stars):", du_lieu.get("stargazers_count"))
    print("Ngôn ngữ chính:", du_lieu.get("language"))
else:
    print("Gọi API thất bại, mã lỗi:", response.status_code)

# Bài tập 5.2 - Vận dụng với API tỷ giá ngoại tệ (Cần kết nối Internet)
print("\n=== BÀI TẬP 5.2: GỌI TỶ GIÁ NGOẠI TỆ API ===")
url_ty_gia = "https://open.er-api.com/v6/latest/USD"

try:
    response_ty_gia = requests.get(url_ty_gia, timeout=10)
    if response_ty_gia.status_code == 200:
        du_lieu_ty_gia = response_ty_gia.json()
        ty_gia_vnd = du_lieu_ty_gia["rates"]["VND"]
        print(f"Tỷ giá thực tế: 1 USD = {ty_gia_vnd:,.0f} VND")
    else:
        print("Không lấy được tỷ giá, mã lỗi:", response_ty_gia.status_code)
except requests.exceptions.RequestException as e:
    print("Lỗi kết nối mạng:", e)