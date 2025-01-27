# 013 - Viết hàm để kiểm tra một số có
# phải là số nguyên tố không
x=int(input())
def ktr(n):
    if n <= 1:
        return 'NO'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'NO'
    return 'YES'
if ktr(x):
    print(f"{x} là số nguyên tố.")
else:
    print(f"{x} không phải là số nguyên tố.")
