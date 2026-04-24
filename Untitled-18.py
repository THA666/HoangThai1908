# cau_f.chu vi hcn
rect_perimeter = lambda d, r: 2 * (d + r)

d = float(input("Nhập chiều dài: "))
r = float(input("Nhập chiều rộng: "))
print(f"Chu vi hình chữ nhật là: {rect_perimeter(d, r)}")