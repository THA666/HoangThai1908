# cau_h.kiem tra so nguyen to
import math
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, math.isqrt(n) + 1))

n = int(input("Nhập số nguyên n: "))
if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} KHÔNG phải là số nguyên tố.")