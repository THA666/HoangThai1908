def generate_strobogrammatic(n, pairs, middles):
    """
    Hàm đệ quy để phát sinh số strobogrammatic có n chữ số
    target_n dùng để kiểm tra xem có đang ở lớp ngoài cùng hay không (để tránh số 0)
    """
    def helper(current_n, target_n):
        if current_n == 0:
            return [""]
        if current_n == 1:
            return middles

        # Lấy danh sách các số ngắn hơn 2 đơn vị
        prev_list = helper(current_n - 2, target_n)
        res = []

        for s in prev_list:
            for p_left, p_right in pairs:
                # Nếu là lớp ngoài cùng, không được thêm số 0 vào đầu
                if current_n == target_n and p_left == '0':
                    continue
                res.append(p_left + s + p_right)
        return res

    return helper(n, n)

def main():
    try:
        n = int(input("Nhập n (2 <= n <= 10): "))
        if not (2 <= n <= 10):
            print("Vui lòng nhập n trong khoảng từ 2 đến 10.")
            return
    except ValueError:
        print("Đầu vào không hợp lệ.")
        return

    # Định nghĩa quy tắc cho số cơ bản
    pairs_basic = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
    middles_basic = ['0', '1', '8']

    # Định nghĩa quy tắc cho số mở rộng
    pairs_ext = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6'), ('2', '2'), ('5', '5')]
    middles_ext = ['0', '1', '8', '2', '5']

    # a. Phát sinh số strobogrammatic cơ bản
    result_a = generate_strobogrammatic(n, pairs_basic, middles_basic)
    print(f"\na.- Có {len(result_a)} số strobogrammatic cơ bản gồm {n} chữ số:")
    print(result_a)

    # b. Phát sinh số strobogrammatic mở rộng
    result_b = generate_strobogrammatic(n, pairs_ext, middles_ext)
    print(f"\nb.- Có {len(result_b)} số strobogrammatic mở rộng gồm {n} chữ số:")
    print(result_b)

if __name__ == "__main__":
    main()