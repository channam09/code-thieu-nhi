# 001 - Viết chương trình để kiểm tra số
#  nguyên dương hay âm

def check_number(n):
    if n > 0:
        return "Số bạn nhập là số dương."
    else:
        return "Số bạn nhập là số âm."  

try:
    number = int(input("Nhập một số nguyên: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")