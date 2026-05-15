def giai_bai_117():
    # Nhập số nguyên dương n
    n_str = input("Nhập số nguyên dương n: ").strip()

    # Kiểm tra dữ liệu hợp lệ
    if not n_str.isdigit() or int(n_str) <= 0:
        print("Vui lòng nhập số nguyên dương lớn hơn 0.")
        return

    tong_S = 0
    bieu_thuc = []

    # Tìm tất cả số con
    for i in range(len(n_str)):
        for j in range(i + 1, len(n_str) + 1):
            sub_str = n_str[i:j]

            so_con = int(sub_str)
            tong_S += so_con ** 2

            # Lưu biểu thức để in ra giống đề
            bieu_thuc.append(f"{sub_str}²")

    # In kết quả giống ví dụ
    print("\nS =", " + ".join(bieu_thuc), "=", tong_S)


# Chạy chương trình
if __name__ == "__main__":
    giai_bai_117()