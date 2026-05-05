from collections import Counter

# Nhập 2 chuỗi từ bàn phím
S1 = input("Nhập chuỗi S1: ")
S2 = input("Nhập chuỗi S2: ")

# a) In ra những ký tự xuất hiện trong cả 2 chuỗi.

dict_c1 = Counter(S1)
dict_c2 = Counter(S2)

# Phép & trả về các phần tử chung
ket_qua_a = dict_c1 & dict_c2
list_chung = list(ket_qua_a.keys())

print(f"\na) Những ký tự xuất hiện trong cả 2 chuỗi: {list_chung}")

# Đưa mỗi chuỗi vào 1 dict để dò tìm
dict1 = dict(dict_c1)
dict2 = dict(dict_c2)

# Tìm ký tự trong S1 nhưng không có trong S2
ds_s1_not_s2 = [char for char in dict1 if char not in dict2]
# Tìm ký tự trong S2 nhưng không có trong S1
ds_s2_not_s1 = [char for char in dict2 if char not in dict1]

# b) Đếm xem có bao nhiêu ký tự có trong S1 nhưng không có trong S2 
count_s1_not_s2 = len(ds_s1_not_s2)
count_s2_not_s1 = len(ds_s2_not_s1)

print(f"b) Số lượng ký tự có trong S1 nhưng không có trong S2: {count_s1_not_s2}")
print(f"   Số lượng ký tự có trong S2 nhưng không có trong S1: {count_s2_not_s1}")

# c) In ra những ký tự có trong S1 nhưng không có trong S2
print(f"c) Ký tự trong S1 không có trong S2: {ds_s1_not_s2}")
print(f"   Ký tự trong S2 không có trong S1: {ds_s2_not_s1}")