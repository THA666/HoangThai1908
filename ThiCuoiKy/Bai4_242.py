# --- 1. KIỂM TRA SỐ ĐỒNG NHẤT (Ví dụ: 111, 2222) ---
# Cách 1: Sử dụng hàm all (Tất cả chữ số phải giống chữ số đầu tiên)
check_dong_nhat_all = lambda k: k > 0 and all(d == str(k)[0] for d in str(k))

# Cách 2: Sử dụng hàm any (Không có bất kỳ chữ số nào khác chữ số đầu tiên)
check_dong_nhat_any = lambda k: k > 0 and not any(d != str(k)[0] for d in str(k))


# --- 2. KIỂM TRA SỐ HOÀN THIỆN (Ví dụ: 6, 28) ---
# Tổng các ước nhỏ hơn n phải bằng chính nó
check_so_hoan_thien = lambda n: n > 1 and sum(i for i in range(1, n) if n % i == 0) == n


# --- CHƯƠNG TRÌNH CHÍNH: DUYỆT TỪ 1 ĐẾN 10000 ---

print("--- DANH SÁCH CÁC SỐ ĐẶC BIỆT TRONG KHOẢNG [1, 10000] ---")

# Liệt kê số đồng nhất
print("\n1. Các số đồng nhất tìm được:")
for i in range(1, 10001):
    # Sử dụng một trong hai cách lambda ở trên để kiểm tra
    if check_dong_nhat_all(i):
        print(i, end=" ")

# Liệt kê số hoàn thiện
print("\n\n2. Các số hoàn thiện tìm được:")
for i in range(1, 10001):
    if check_so_hoan_thien(i):
        print(i, end=" ")
print() # Xuống dòng kết thúc