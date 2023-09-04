# Bài 34
# Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương
# Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”
def bai34():
    a = int(input("Nhập a:"))
    while a < 0:
        a = int(input("Nhập a:"))
        if a > 0: print("Bạn nhập đúng quy tắc")
# bai34()

# Bài 35
# Nhập n. Cho S(k) = 1 + 2 + 3 + … + k
# Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
def bai35():
    n = int(input("N=: "))
    while n < 0:
        n = int(input("Nhập lại n: "))
    
    S = 0
    k = 0
    while S + k < n:
        k += 1
        S = S + k
    
    print("S(k) lớn nhất nhưng nhỏ hơn n:", S)

# bai35()

# Bài 36
# Nhập vào A, tìm n nhỏ nhất sao cho
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
def bai36():
    A = float(input("Nhập A:"))
    n = 0
    S = 0
    while S <= A:
        n += 1
        S += 1/n
        print("n nhỏ nhất là:", n)

# bai36()

# Bài 37
# Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.
# Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
def bai37():
    max_num = float('-inf')
    min_num = float('inf')
    while True:
        num = int(input("Nhập số nguyên (Nhập -1 để kết thúc):"))
        if num == -1:break 
        if num > max_num: max_num = num
        if num < min_num: min_num = num
    if max_num == float('-inf') or min_num == float('inf'):print("Bạn chưa nhập số nào")
    else:print("Số lớn nhất là:", max_num,"\nSố nhỏ nhất là:",min_num)
# bai37()

# Bài 38: Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số
def bai38():
    n = int(input("N=: "))
    dem = 0
    while n >= 10:
        n /= 10
        dem +=1
        print("số có",dem +1,"ký tự")
# bai38()

# Bài 39: Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
def bai39():
    n = int(input("N=: "))
    chan = 0
    le = 0
    while n > 0:
        socuoi = n % 10
        if socuoi % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10
    print("Số chẵn:", chan,"\nSố lẻ:", le,"\nTổng các số:",chan+le)
# bai39()


# Bài 40: Nhập vào số nguyên dương n, tính tổng các chữ số của n
def bai40():
    n = int(input("N=: "))
    nn = n
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    print("Tổng các chữ số của",nn,"=",tong)
# bai40()
        

# Bài 41: Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không
def bai41():
    n = int(input("N="))
    a=n
    while n % 2 == 0:
        n //= 2
    if n == 1:
        print(a,"là dạng 2^k")
    else:
        print(a,"không phải là dạng 2^k")
# bai41()
        

# Bài 42:Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó
# Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A
def bai42():
    a = int(input("A="))
    fib1 = 1
    fib2 = 1
    max_fib = 1

    while True:
        next_fib = fib1 + fib2
        if next_fib <= a:
            max_fib = next_fib
            fib1 = fib2
            fib2 = next_fib
        else:
            break

    print("Số Fibonacci lớn nhất không vượt quá",a,"=", max_fib)
bai42()