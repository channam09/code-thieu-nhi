# 004 - Chương trình tính tiền taxi dựa
#  trên số km đã đi

def check_number(n):
    s=0
    if n==1:
        s=10000
    elif n>1 and n<=10:
        s=10000+(n-1)*8500
    else:
        s=10000+(9)*8500+(n-10)*7500
    return(s)
try:
    # number = int(input("Nhập một số nguyên: "))
    number = 15
    result = check_number(number)
    print(" Tổng tiền taxi là",result,"VNĐ")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")