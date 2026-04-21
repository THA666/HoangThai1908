def chuan_hoa_dong(line):
    line = line.strip()

    # Chuẩn hóa nhiều space → 1 space
    words = line.split()
    line = " ".join(words)

    result = ""
    for i in range(len(line)):
        if line[i] in ".,":  
            # Xóa space trước dấu
            if result.endswith(" "):
                result = result[:-1]
            result += line[i]
        else:
            result += line[i]

    return result


# MAIN
print("Nhap nhieu dong (Enter rong de dung):")
lines = []

while True:
    s = input()
    if s == "":
        break
    lines.append(chuan_hoa_dong(s))

print("\nChuoi hoan chinh:")
for line in lines:
    print(line)