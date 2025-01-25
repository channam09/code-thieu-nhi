# 008 - Viết chương trình để đếm số
# lượng số chẵn và lẻ trong một danh
# sách
def KTR(numbers):
    chan = 0
    le = 0
    for number in numbers:
        if number % 2 == 0:
            chan += 1
        else:
            le += 1
    return chan, le
# Nhập danh sách các số nguyên từ người dùng

numbers = list(map(int,input().split()))
even_count, odd_count = KTR(numbers)
print(f"Số lượng số chẵn: {even_count}")
print(f"Số lượng số lẻ: {odd_count}")