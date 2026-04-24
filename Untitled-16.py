# cau_d.cho biet boi so cau 13 va 19 hay khong
is_multiple = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhập số nguyên n: "))
if is_multiple(n):
    print(f"{n} là bội số của 13 hoặc 19.")
else:
    print(f"{n} KHÔNG là bội số của 13 hoặc 19.")