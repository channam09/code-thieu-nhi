# 005 - Viết chương trình để tính điểm
#  trung bình và xếp loại học sinh.


def ktr(diem):
    if diem >= 8.5:
        return "Xuất sắc"
    elif diem >= 7.0:
        return "Giỏi"
    elif diem >= 5.5:
        return "Khá"
    elif diem >= 4.0:
        return "Trung bình"
    else:
        return "Yếu"
    

try:
    # scores = []
    # somon = int(input("Nhập số lượng môn học: "))
    # if somon <= 0:
    #     print("Số lượng môn học phải lớn hơn 0.")
    # else:
    #     for i in range(somon):
    #         score = float(input(f"Nhập điểm môn học thứ {i+1}: "))
    number = [5,7,6,6.5]
    diemtong=sum(number)/len(number)
    result = ktr(diemtong)
    print(result)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")