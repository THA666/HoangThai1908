# cau_e.tinh dien tich hinh tron
import math
circle_area = lambda r: math.pi * r**2

r = float(input("Nhập bán kính hình tròn r: "))
print(f"Diện tích hình tròn là: {circle_area(r):.2f}")