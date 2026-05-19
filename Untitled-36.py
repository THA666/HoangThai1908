def solve_strobogrammatic():
    LIMIT = 1000000

    # ==========================================
    # 1. SÀNG ERATOSTHENES
    # Tìm các số nguyên tố nhỏ hơn 1 triệu
    # ==========================================
    is_prime = [True] * LIMIT

    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, int(LIMIT ** 0.5) + 1):

        if is_prime[p]:

            for i in range(p * p, LIMIT, p):
                is_prime[i] = False

    # ==========================================
    # 2. BẢNG QUY TẮC XOAY
    # ==========================================

    # Strobogrammatic cơ bản
    map_basic = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    # Strobogrammatic mở rộng
    map_ext = {
        '0': '0',
        '1': '1',
        '2': '2',
        '5': '5',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    # ==========================================
    # 3. HÀM XOAY SỐ 180 ĐỘ
    # ==========================================
    def get_rotated_value(n, mapping):

        s = str(n)

        rotated = ""

        # Duyệt ngược chuỗi
        for ch in reversed(s):

            # Nếu chữ số không xoay được
            if ch not in mapping:
                return None

            rotated += mapping[ch]

        return int(rotated)

    # ==========================================
    # 4. DANH SÁCH KẾT QUẢ
    # ==========================================
    list_a = []   # Strobogrammatic cơ bản
    list_b = []   # Nguyên tố strobogrammatic cơ bản

    list_c = []   # Strobogrammatic mở rộng
    list_d = []   # Nguyên tố strobogrammatic mở rộng

    list_e = []   # Theo yêu cầu câu e

    # ==========================================
    # 5. DUYỆT TỪNG SỐ
    # ==========================================
    for i in range(1, LIMIT):

        # --------------------------------------
        # a, b : STROBOGRAMMATIC CƠ BẢN
        # --------------------------------------
        rot_basic = get_rotated_value(i, map_basic)

        if rot_basic == i:

            list_a.append(i)

            if is_prime[i]:
                list_b.append(i)

        # --------------------------------------
        # c, d, e : STROBOGRAMMATIC MỞ RỘNG
        # --------------------------------------
        rot_ext = get_rotated_value(i, map_ext)

        if rot_ext is not None:

            # c, d : Là số strobogrammatic mở rộng
            if rot_ext == i:

                list_c.append(i)

                if is_prime[i]:
                    list_d.append(i)

            # e :
            # Không phải strobogrammatic
            # Không phải nguyên tố
            # Nhưng xoay xong là số nguyên tố
            elif rot_ext < LIMIT:

                if (not is_prime[i]) and is_prime[rot_ext]:

                    list_e.append(i)

    # ==========================================
    # 6. IN KẾT QUẢ
    # ==========================================

    print("=" * 60)
    print("a. CAC SO STROBOGRAMMATIC CO BAN < 1,000,000")
    print("=" * 60)

    print("Tong so:", len(list_a))
    print("20 so dau tien:")
    print(list_a[:20])

    print()

    print("=" * 60)
    print("b. CAC SO NGUYEN TO STROBOGRAMMATIC CO BAN")
    print("=" * 60)

    print("Tong so:", len(list_b))
    print(list_b)

    print()

    print("=" * 60)
    print("c. CAC SO STROBOGRAMMATIC MO RONG < 1,000,000")
    print("=" * 60)

    print("Tong so:", len(list_c))
    print("20 so dau tien:")
    print(list_c[:20])

    print()

    print("=" * 60)
    print("d. CAC SO NGUYEN TO STROBOGRAMMATIC MO RONG")
    print("=" * 60)

    print("Tong so:", len(list_d))
    print(list_d)

    print()

    print("=" * 60)
    print("e. KHONG PHAI STROBOGRAMMATIC,")
    print("   KHONG PHAI NGUYEN TO,")
    print("   NHUNG XOAY 180 DO LA SO NGUYEN TO")
    print("=" * 60)

    print("Tong so:", len(list_e))
    print("20 so dau tien:")
    print(list_e[:20])


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":

    solve_strobogrammatic()