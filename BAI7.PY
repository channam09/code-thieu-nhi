# 007 - Viết chương trình để kiểm tra
# một năm có phải năm nhuận không
def KTR(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return True
    else:
        return False
# Nhập năm từ người dùng
# year = int(input("Nhập một năm: "))
year=2024
if KTR(year):
    print(f"Năm {year} là năm nhuận.")
else:
    print(f"Năm {year} không phải là năm nhuận.")