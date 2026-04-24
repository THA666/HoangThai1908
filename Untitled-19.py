# cau_g.kiem tra so chinh phuong
import math
is_perfect_square = lambda n: n >= 0 and math.isqrt(n)**2 == n

n = int(input("Nhập số nguyên n: "))
if is_perfect_square(n):
    print(f"{n} là số chính phương.")
else:
    print(f"{n} KHÔNG phải là số chính phương.")