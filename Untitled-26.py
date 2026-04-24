def fibonacci(n):
    # Điều kiện dừng (Base case) theo định nghĩa trong ảnh: F0 = F1 = 1
    if n == 0 or n == 1:
        return 1
    # Bước đệ quy (Recursive step): Fn = Fn-1 + Fn-2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# --- CHƯƠNG TRÌNH CHÍNH ---
try:
    n_input = int(input("Nhập số nguyên dương n: "))
    
    if n_input <= 0:
        print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    else:
        # Theo ví dụ trong ảnh: 
        # Số hạng thứ 1 (n=1) là F0
        # Số hạng thứ 7 (n=7) là F6 = 13
        # Vì vậy ta gọi hàm với giá trị (n_input - 1) để khớp với ví dụ
        ket_qua = fibonacci(n_input - 1)
        print(f"Số hạng thứ {n_input} của chuỗi Fibonacci là: {ket_qua}")

except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên!")