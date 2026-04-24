def luy_thua(a, b):
    if b == 0:
        return 1
    return a * luy_thua(a, b - 1)

# Test
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print(f"{a}^{b} =", luy_thua(a, b))