import math

# --- HÀM KIỂM TRA SỐ NGUYÊN TỐ ---
def kiem_tra_snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Ý 1: IN BẢNG CỬU CHƯƠNG
print("--- BẢNG CỬU CHƯƠNG ---")
nhap_ab = input("Nhập a, b: ")
danh_sach = nhap_ab.split(',')
a = int(danh_sach[0].strip())
b = int(danh_sach[1].strip())

if a < b:
    for i in range(a, b + 1):
        print(f"Bảng cửu chương {i}:")
        for j in range(1, 11): print(f"{i} x {j} = {i*j}")
        print("-" * 15)
else:
    for i in range(b, a + 1):
        print(f"Bảng cửu chương {i}:")
        for j in range(1, 11): print(f"{i} x {j} = {i*j}")
        print("-" * 15)

# Ý 2: LIỆT KÊ CÁC SỐ NGUYÊN TỐ < n
print("\n--- LIỆT KÊ SỐ NGUYÊN TỐ NHỎ HƠN n ---")
n_cau2 = int(input("Nhập n: "))

print(f"Các số nguyên tố < {n_cau2} là:")
for i in range(2, n_cau2):
    if kiem_tra_snt(i):
        print(i, end=" ")
print() 

# Ý 3: LIỆT KÊ CÁC ƯỚC SỐ CỦA n LÀ SỐ NGUYÊN TỐ
print("\n--- LIỆT KÊ ƯỚC SỐ CỦA n LÀ SỐ NGUYÊN TỐ ---")
n_cau3 = int(input("Nhập n: "))

uoc_snt = []
for i in range(2, n_cau3 + 1):
    # Kiểm tra đồng thời: i là ước của n VÀ i là số nguyên tố
    if n_cau3 % i == 0 and kiem_tra_snt(i):
        uoc_snt.append(str(i))

# In kết quả
ket_qua_uoc = ", ".join(uoc_snt)
print(f"Các số vừa là ước của {n_cau3}, vừa là số nguyên tố: {ket_qua_uoc}")