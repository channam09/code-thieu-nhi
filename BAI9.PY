# 009 - Viết chương trình để in tất cả
# các số nguyên tố từ 1 đến 100
def KTR(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for number in range(1, 101):
    if KTR(number):
        print(number, end=' ')
        print()