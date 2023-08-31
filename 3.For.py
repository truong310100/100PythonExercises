# Bài 23:In 10 lần chữ hello ra màn hình
def bai23():
    for a in range(10):
        print("hello",a)

# Bài 24: In các số lẻ dương bé hơn 100
def bai24():
    for a in range(100):
        if a%3==0:print(a)

# Bài 25: In các số chẵn chia hết cho 3 bé hơn 100
def bai25():
    for a in range(100):
        if a%2==0 and a%3==0:print(a)

#Bài 26: Nhập vào số nguyên dương a, in ra bảng cửu chương của a
def bai26():
    a = int(input("Nhập a:"))
    for i in range(1,11):print(a,"*",i,"=",a*i)

# Bài 27
# Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
# Ví dụ: Ta nhập h = 4:
# ** **********
def bai27():
    h = int(input("Nhập độ cao h: "))
    for i in range(1,h + 1):print("*" * i)


# Bài 28
# Nhập vào n
# Tính S = 1 + 2 + 3 + 4 + … + n
def bai28():
    n = int(input("Nhập n:"))
    total = 0
    for i in range(n):total += i + 1
    print(total)

# Bài 29: Nhập vào số nguyên dương a, in toàn bộ ước của a
def bai29():
    a = int(input("Nhập a: "))
    print("Các ước của", a, "là:")
    for i in range(1, a + 1):
        if a % i == 0:
            print(i)

# Bài 30: Nhập vào số nguyên dương a, đếm số ước của a
def bai30():
    a = int(input("Nhập a: "))
    print("Các ước của", a, "là:")
    total = 0
    for i in range(1, a + 1):
        if a % i == 0:
            total +=1
            print(i)
    print("Số ước của", a, "là:", total)

# Bài 31: Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
def bai31():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b:"))
    print("Các ước của", a ,"và",b, "là:")
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            print(i)

# Bài 32: Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
def bai32():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b:"))
    print("Các ước của", a ,"và",b, "là:")
    total = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            total += 1
            print(i)
    print("Số ước của", a,"và",b, "là:", total)


# Bài 33: Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
def bai33():
    a = int(input("Nhập a: "))
    if a <= 1:
        print("Không phải là số nguyên tố")
    else:
        is_prime = True
        for p in range(2, int(a ** 0.5) + 1):
            if a % p == 0:
                is_prime = False
                break
        
        if is_prime:
            print("a là số nguyên tố")
        else:
            print("a không phải là số nguyên tố")
bai33()