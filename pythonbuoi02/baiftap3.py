# bài 3.1
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))
print(int(so_thuc)) 
#bài 3.2
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a)) 
print(round(b))
print(round(b, 2)) 
print(pow(c, 2))
print(divmod(c, d))
# bài 3.3
import math
a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")