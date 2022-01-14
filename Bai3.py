def ThuanNghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;
name = 'Nguyen Dai Nhan'
print(name)
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", ThuanNghich(n));
