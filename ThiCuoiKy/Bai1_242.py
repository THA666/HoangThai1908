# Nhập dữ liệu đầu vào
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
n = int(input("Số lượng số lẻ cần hiển thị: "))

# Tính toán
dien_tich_day = dai * rong
the_tich = dien_tich_day * cao

# Xuất kết quả với định dạng làm tròn n chữ số lẻ
# Sử dụng Unicode \u00b2 cho mũ 2 và \u00b3 cho mũ 3
print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.{n}f} cm\u00b2")
print(f"Thể tích hình khối = {the_tich:.{n}f} cm\u00b3")