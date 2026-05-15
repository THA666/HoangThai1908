import math

def so_dao_nguoc(n):
    # Chuyển số thành chuỗi, đảo ngược chuỗi và chuyển lại thành số nguyên
    return int(str(n)[::-1])

def giai_bai_114():
    try:
        # Nhập vào hai số nguyên a và b
        dong_nhap = input("Nhập hai số a và b (cách nhau bởi khoảng trắng): ").split()
        if len(dong_nhap) < 2:
            print("Vui lòng nhập đủ 2 số.")
            return
            
        a = int(dong_nhap[0])
        b = int(dong_nhap[1])

        # Kiểm tra điều kiện đề bài: 10 <= a <= b <= 30000
        if not (10 <= a <= b <= 30000):
            print("Lưu ý: Đề bài yêu cầu 10 <= a <= b <= 30000.")
            # Ta vẫn tiếp tục tính toán theo a, b thực tế người dùng nhập

        danh_sach_than_thien = []

        # Duyệt qua các số từ a đến b
        for i in range(a, b + 1):
            dao_i = so_dao_nguoc(i)
            # Kiểm tra nếu UCLN của số đó và số đảo ngược là 1
            if math.gcd(i, dao_i) == 1:
                danh_sach_than_thien.append(i)

        # In kết quả
        print(f"\nCác số thân thiện trong khoảng từ {a} đến {b} là:")
        # In các số cách nhau bởi dấu phẩy hoặc khoảng trắng
        print(", ".join(map(str, danh_sach_than_thien)))
        
        print(f"\nSố lượng số thân thiện đã in ra: {len(danh_sach_than_thien)}")

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số nguyên.")

# Chạy chương trình
if __name__ == "__main__":
    giai_bai_114()