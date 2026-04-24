def tong_chu_so(n):
    if n == 0:
        return 0
    return n % 10 + tong_chu_so(n // 10)

# Test
n = int(input("Nhập n: "))
print("Tổng chữ số =", tong_chu_so(abs(n)))