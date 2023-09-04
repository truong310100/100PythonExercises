# Bài 43: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ 
# (quy định là chuỗi không có ký tự đặc biệt, không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)
def bai43():
    strings = str(input("Nhập chuỗi:"))
    print(len(strings))
# bai43()

# Bài 44: Nhập vào một chuỗi, hãy in từ đầu tiên trong chuỗi
def bai44():
    strings = str(input("Nhập chuỗi:"))
    print("Từ đầu tiên là",strings[0])
# bai44()

# Bài 45: Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
# VD:Nhập: 3, 12, 15 Tổng: 30
def bai45():
    string = input("Nhập số chuỗi:")
    numbers = string.split(",")
    sum = 0
    for i in numbers:
        sum += int(i)
    print(sum)
# bai45()

# Bài 46: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
def bai46():
    strings = str(input("Nhập chuỗi:"))
    inSupper = 0
    inLower = 0
    inDigit = 0
    for char in strings:
        if char.isupper(): inSupper += 1
        elif char.islower(): inLower += 1
        elif char.isdigit(): inDigit += 1
    print("In Hoa=",inSupper,"\nIn Thường =",inLower,"\nSố =",inDigit,"\nTổng =",len(strings))
# bai46()

# Bài 47: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
# def bai47():
# bai47()

# Bài 48: Nhập vào một chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
# VD:Nhập chuỗi: abd45ecf47wde3s1 - Tổng: 4 + 5 + 4 + 7 + 3 + 1 = 24
def bai48():
    strings = str(input("Nhập chuỗi:"))
    inDigit = 0
    sum = 0
    for char in strings:
        if char.isdigit():
            sum += int(char)
            inDigit += 1
    print("Tổng các ký tự số là:", sum)
# bai48()

# Bài 49: Nhập vào một chuỗi, hãy tách toàn bộ con số trong chuỗi ra rồi tính tổng của chúng
# VD:Nhập chuỗi: abd45ecf47wde3s1 - Tổng: 45 + 47 + 3 + 1 = 96
def bai49():
    import re
    strings = str(input("Nhập chuỗi:"))
    numbers = re.findall(r'\d+', strings)
    total = sum(map(int, numbers))
    print("Tổng các con số là:", total)
# bai49()

# Bài 50: Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là một chuỗi mật khẩu mạnh hay không
# (một chuỗi mật khẩu mạnh cần có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 1 con số, 1 chữ thường và độ dài phải lớn hơn 6)

def bai50():
    import re
    password = str(input("Nhập mật khẩu: "))
    noti = "Mật khẩu yếu, yêu cầu phải có ít nhất:\n1 ký tự đặc biệt.\n1 ký tự in hoa.\n1 con số.\n1 chữ thường.\nđộ dài phải lớn hơn 6."
    if len(password) <= 6:print(noti)
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):print(noti)
    elif not re.search(r'[A-Z]', password):print(noti)
    elif not re.search(r'\d', password):print(noti)
    elif not re.search(r'[a-z]', password):print(noti)
    else:print("Mật khẩu mạnh")
# bai50()


# Bài 51: Nhập vào một số nguyên, hãy chuyển số sang chuỗi, rồi đặt dấu chấm phân tách mỗi 3 chữ số 
# (phân cách phần ngàn) rồi in ra màn hình
# VD: Nhập số: 375469485 - Đổi sang chuỗi rồi in ra: 375.469.485
def bai51():
    number = int(input("Nhập số nguyên: "))
    number_str = str(int(number))
    
    formatted_str = ""
    count = 0

    for digit in reversed(number_str):
        if count == 3:
            formatted_str = "." + formatted_str
            count = 0
        formatted_str = digit + formatted_str
        count += 1

    print("Đã chuyển", formatted_str)
# bai51()

# Bài 52: Nhập vào chuỗi a và chuỗi b
# Hãy xóa chuỗi b trong chuỗi a rồi in lại chuỗi a ra màn hình (không dùng hàm replace)
# Ví dụ:
# Chuỗi a: "Xin chào mọi người!"
# Chuỗi b: "Xin chào"
# Sau khi xóa, chuỗi a: " mọi người!"
def bai52():
    a = input("Nhập chuỗi a: ")
    b = input("Nhập chuỗi b: ")
    index = a.find(b)
    if index == -1:
        print("Chuỗi b không tồn tại trong chuỗi a.")
    else:
        part1 = a[:index]
        part2 = a[index + len(b):]
        print("Sau khi xóa, chuỗi a:", part1 + part2)
bai52()
