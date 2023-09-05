# Bài 53: Nhập vào một list số nguyên L, tìm và in ra giá trị lớn nhất trong L
def bai53():
    L = [int(x) for x in input("Nhập danh sách (cách nhau dấu phẩy): ").split(",")]
    if not L: print("Danh sách rỗng")
    else:
        max_number = [0]
        for num in L:
            if num > max_number:max_number=num
            print("Giá trị lớn nhất trong danh sách là:",max_number)
bai53()

# Bài 54:Nhập vào một list số nguyên L, nhập vào 2 số nguyên dương a và b (a < b < len(L))
# Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b
# def bai54():
# bai54()

# Bài 55:Nhập vào một list số nguyên L, hãy kiểm tra xem tất cả các phần tử trong mảng có bằng nhau hay không, nếu có thì in True, không có thì in False
# def bai55():
# bai55()

# Bài 56:Nhập vào một list số nguyên L, tìm và in ra giá trị dương đầu tiên của list, nếu không có giá trị dương, ta in ra -1
# def bai56():
# bai56()

# Bài 57: Nhập vào một list L, hãy tìm và in ra giá trị âm lớn nhất trong L, nếu L không có giá trị âm thì ta in 0
# def bai57():
# bai57()

# Bài 58: Nhập vào một list số nguyên L, nhập vào số nguyên x, tìm giá trị trong list xa x nhất
# def bai58():
# bai58()

# Bài 59: Nhập vào một list số nguyên L, tính giá trị trung bình của list L
# def bai59():
# bai59()

# Bài 60: Nhập vào một list số nguyên L, hãy kiểm tra xem L có được sắp xếp từ bé đến lớn hay không, nếu có thì in True, không có thì in False
# def bai60():
# bai60()

# Bài 61: Nhập vào một list số nguyên L, hãy sắp xếp list L theo thứ tự từ bé đến lớn
# def bai61():
# bai61()

# Bài 62: Nhập vào một list số nguyên L, hãy kiểm tra xem L có phải là một cấp số cộng hay không? Nếu có thì tìm và in ra công sai, nếu không có thì in ra None
# def bai62():
# bai62()

# Bài 63: Nhập vào một list số nguyên L, Hãy tìm và in ra một vị trí trong L thỏa hai điều kiện: có hai giá trị lân cận và giá trị tại vị trí đó bằng tích hai giá trị lân cận. Nếu L không tồn tại giá trị như vậy thì in ra - 1
# def bai63():
# bai63()

# Bài 64: Người ta định nghĩa một list số nguyên là list chẵn lẻ, nếu như tổng 2 phần tử bất kỳ bên trong list đều là số lẻ
# Nhập vào một list số nguyên L và kiểm tra xem L có phải là list chẵn lẻ hay không
# def bai64():
# bai64()

# Bài 65: Người ta định nghĩa một list số nguyên được gọi là “dạng sóng” khi tất cả các phần tử đều lớn hơn hoặc nhỏ hơn hai phần tử xung quanh nó.
# Nhập vào một list số nguyên L và kiểm tra xem L có phải là list “dạng sóng” hay không, nếu có thì ta in ra True, không có thì ta in False
# def bai65():
# bai65()

# Bài 66: Nhập vào một list số nguyên L, hãy đếm số lượng giá trị trong list thỏa tính chất: “lớn hơn tất cả các giá trị đứng đằng trước nó”
# def bai66():
# bai66()

# Bài 67: Nhập vào một list số nguyên L, hãy đưa các số chẵn trong list về đầu list, số lẻ về cuối list và các phần tử 0 nằm ở giữa
# def bai67():
# bai67()

# Bài 68: Nhập vào một list số nguyên L, hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất
# def bai68():
# bai68()

# Bài 69: Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy tìm và in ra chuỗi có độ dài lớn nhất và số nguyên có giá trị nhỏ nhất
# def bai69():
# bai69()

# Bài 70: Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy kiểm tra các phần tử trong L có phải là chuỗi và số xen kẽ nhau không, nếu có thì ta tiến hành tạo một list K mới có các phần tử như sau:
# K[i/2] = L[i]*L[i+1] (với i chẵn)
# def bai70():
# bai70()

# Bài 71: Nhập vào một list L có các phần tử là chuỗi (các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng)
# Hãy tìm ra vị trí của chuỗi có nhiều từ nhất
# def bai71():
# bai71()

# Bài 72: Nhập vào một list L có các phần tử là chuỗi. Hãy tìm ra chuỗi có vị trí ký tự in hoa lớn nhất
# def bai72():
# bai72()
