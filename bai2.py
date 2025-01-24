# 001 - 002 - Viết chương trình để kiểm tra số
#  chẵn hay lẻ

def check_number(n):
    if n%2==0:
        return "Số bạn nhập là số chẵn."
    elif n%2!=0:
        return "Số bạn nhập là số lẻ."
    

try:
    # number = int(input("Nhập một số nguyên: "))
    number = 15
    result = check_number(number)
    print(result)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")