# --- 1. Hàm lambda nhận n, kiểm tra là bội số của 13 hoặc 19 ---
# n % 13 == 0 nghĩa là n chia hết cho 13
check_boi_so = lambda n: n % 13 == 0 or n % 19 == 0

# Kiểm tra điều kiện tam giác trước -> Đều -> Cân -> Vuông -> Thường
phan_loai_tam_giac = lambda a, b, c: (
    "Tam giác Đều" if a == b == c else
    "Tam giác Cân" if a == b or b == c or a == c else
    "Tam giác Vuông" if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2) else
    "Tam giác Thường"
) if (a + b > c and a + c > b and b + c > a) else "Không phải tam giác"

# kiểm tra bội số
n = int(input("Nhập số nguyên n để kiểm tra bội 13 hoặc 19: "))
if check_boi_so(n):
    print(f"{n} là bội số của 13 hoặc 19")
else:
    print(f"{n} không phải bội số của 13 hoặc 19")

# kiểm tra tam giác
print("\nNhập 3 cạnh tam giác để phân loại:")
a = int(input("Cạnh a: "))
b = int(input("Cạnh b: "))
c = int(input("Cạnh c: "))

ket_qua = phan_loai_tam_giac(a, b, c)
print(f"Kết quả phân loại: {ket_qua}")