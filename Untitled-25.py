def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Test
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN =", gcd(a, b))