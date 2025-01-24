# 003 - Viết chương trình để tìm số lớn
#  nhất trong ba số

def check_number(x,y,z):
    n=max(x,y)
    m=max(n,z)
    return(m)
try:
    # a = int(input("Nhập một số nguyên: "))
    # b = int(input("Nhập một số nguyên: "))
    # c = int(input("Nhập một số nguyên: "))
    a = 15
    b = 10
    c = 5
    result = check_number(a,b,c)
    print('số lớn nhất trong ba số là',result)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")