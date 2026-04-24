# cau_i.Kiem tra loai tam giac
def classify_triangle(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        return "Không phải 3 cạnh tam giác hợp lệ"

    if a == b == c:
        return "Tam giác đều"
    elif a == b or b == c or a == c:
        if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            return "Tam giác vuông cân"
        return "Tam giác cân"
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return "Tam giác vuông"
    return "Tam giác thường"


print("\ni) Kiểm tra loại tam giác:")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
print(f"-> Kết quả: {classify_triangle(a, b, c)}")