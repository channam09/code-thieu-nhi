# 016 - Viết hàm để kiểm tra một chuỗi
# có phải là palindrome không
s=input()
if s == s[::-1]:
    print(f'"{s}" là palindrome.')
else:
    print(f'"{s}" không phải là palindrome.')