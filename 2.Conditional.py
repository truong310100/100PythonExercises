# Bài 13:Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì ta in ra đây là số lớn hơn 10
def bai13():
    a = int(input("Nhập a:"))
    if (a > 10): print("Đây là số lớn hơn 10")
    elif (a == 10): print("Đây là số bằng 10")
    else : print("Đây là số nhỏ hơn 10")

# Bài 14: Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
def bai14():
    a=int(input("Nhập a:"))
    if a%2==0 : print("Đây là số chẵn")
    else: print("Đây là số lẻ")

# Bài 15: Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
def bai15():
    a = float(input("Nhập a:"))
    b = float(input("Nhập b:"))
    c = float(input("Nhập c:")) 
    if a + b > c and a + c > b and b + c > a:
        print("Cấu thành độ dài của 1 tam giác")
    else:
        print("Không cấu thành độ dài của 1 tam giác")

# Bài 16: Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)
def bai16():
    a = float(input("Nhập a:"))
    b = float(input("Nhập b:"))
    c = float(input("Nhập c:")) 
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Tam giác đều")
        elif a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Tam giác vuông cân")
            else:
                print("Tam giác cân")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Tam giác vuông")
        else:
            print("Tam giác thường")
    else:
        print("Đây không phải là tam giác")

# Bài 17: Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
def bai17():
    a = int(input("Nhập a:"))
    b = int(input("Nhập b:"))
    c = int(input("Nhập c:")) 
    if a <= b and a <= c:
        if b <= c: print(a,b,c)
        else:print(a,c,b)
    elif b <= a and b <= c:
        if a <= c: print(b,a,c)
        else:print(b,c,a)
    else:
        if a <= b:print(c,a,b)
        else:print(c,b,a)
    
# Bài 18: Giải và biện luận phương trình ax + b = 0
def bai18():
    a = int(input("Nhập a:"))
    b = int(input("Nhập b:"))
    x = float(-b/a)
    print("Áp dụng vào phương trình a x + b = 0, ta có:\n",a,"x +",b,"=0","\n   x     = -b / a","\n   x     = -",b,"/",a,"\n   x     =",x)

# Bài 19: Giải và biện luận phương trình ax^2 + bx + c = 0
import math 
def bai19():
    a = int(input("Nhập a:"))
    b = int(input("Nhập b:"))
    c = int(input("Nhập c:"))
    delta = b**2 - 4 * a * c
    if delta < 0: print("delta =",delta,"< 0","=> PTVN")
    elif delta == 0: print("delta =",delta,"= 0","Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
    else:print("delta =",delta,"> 0","Phương trình có hai nghiệm phân biệt:\n""x1 = ", (-(b) + math.sqrt(delta))/(2*a),"\nx2 = ", (-(b) - math.sqrt(delta))/(2*a))

# Bài 20: Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
def bai20():
    month = int(input("Nhập tháng:"))
    year = int(input("Nhập năm:"))
    if 0 < month > 12:print("Tháng không hợp lệ")
    elif 0 > year:print("Năm không hợp lệ")
    else:
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days_in_month[2] = 29  # Năm nhuận
        print("Tháng", month ,"năm" ,year, "có",days_in_month[month], "ngày.")

# Bài 21: Nhập vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày (giả sư năm đó không phải là năm nhuận)
def bai21():
    day = int(input("Nhập ngày:"))
    month = int(input("Nhập tháng:"))
    if 0 < day > 31:print("Ngày không hợp lệ")
    elif 0 < month > 12:print("Tháng không hợp lệ")
    else:
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            days_in_month[2] = 28  # Không là năm nhuận
        if day > days_in_month[month]:print("Ngày không hợp lệ cho tháng này.")
        else:
            days_to_start = sum(days_in_month[:month]) + day
            print(f"Số ngày cách ngày đầu năm là: {days_to_start}")

# Bài 22
# Nhập điểm toán, văn, anh.
# Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:
# Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
# Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
# Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
# Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
# Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”
def bai22():
    toan = float(input("Nhập điểm toán:"))
    van = float(input("Nhập điểm văn:"))
    anh = float(input("Nhập điểm anh:"))
    if 0 < toan > 10 : print("Điểm toán không hợp lệ")
    elif 0 < van > 10 : print("Điểm văn không hợp lệ")
    elif 0 < anh > 10 : print("Điểm anh không hợp lệ")
    else:
        dtb=(toan+van+anh)/3;print("Điểm trung bình:" ,dtb)
        if dtb >= 8 and toan and van and anh > 6.5:print("Học Sinh Giỏi")
        elif dtb >= 6.5 and (toan >= 6.5 or van >= 6.5) and toan > 5 and van > 5 and anh > 5 : print("Học sinh Khá")
        elif dtb >= 5 and (toan >= 5 or van >= 5) and toan > 3.5 and van > 3.5 and anh > 3.5 : print("Học Sinh Trung Bình")
        elif dtb >= 3.5 and (toan >= 3.5 or van >= 3.5) and toan > 2 and van > 2 and anh > 2 : print("Học Sinh Yếu")
        else : print("Học Sinh Kém")

bai22()