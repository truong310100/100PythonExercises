#Bài 1: Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
def bai1():
    inputNumber = int(input('Input number:'))
    count = (inputNumber*3)+1
    print("Result:", count)

# Bài 2: Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
def bai2():
    inputNumber = int(input('Input number:'))
    count = (inputNumber*inputNumber)/3 #Nếu lấy số nguyên thì thêm // thay cho / hoặc thay biến int bằng float
    print("Result:", count)

# Bài 3: Nhập vào nhiệt độ c, in ra nhiệt độ F
def bai3():
    inputC = int(input('Input C:'))
    convert = (inputC * 9/5) + 32
    print("Result temperature:",convert,"°F")

# Bài 4: Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False
def bai4():
    a = int(input("Input number:"))
    if a%2==0:print(True)
    else :print(False)
    

# Bài 5: Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
def bai5():
    a = int(input("Input number:"))
    if a % 3 == 0 and 50 <= a <= 100:print(True)
    else :print(False)

# Bài 6: Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
def bai6():
    a = int(input("Input number:"))
    if a % 5 == 0 and not (20 <= a <= 70):print(True)
    else :print(False)

# Bài 7: Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
def bai7():
    a = int(input("Input number a:"))
    b = int(input("Input number b:"))
    if a % 2 == 0 or b % 2 == 0 : print(True)
    else :print(False)

# Bài 8: Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
def bai8():
    a = float(input("Input number:"))
    if a == int(a):print(True)
    else :print(False)

# Bài 9: Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
def bai9(n):
    if n < 0:
        return False
    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n

n = int(input("Input number:"))
if bai9(n):
    print("True")
else:
    print("False")


# Bài 10: Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại
# def bai10():

# Bài 11: Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó
# def bai11():

# Bài 12: Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
# def bai12():


# Gọi hàm để thực thi
bai9()