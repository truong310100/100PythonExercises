import pyperclip

def create_def():
    start, end = input("Nhập số đầu và số cuối (cách nhau bằng dấu -): ").split("-")
    start = int(start)
    end = int(end)
    code = ""
    for number in range(start, end + 1):
        function_name = f"bai{number}()"
        function_name = function_name.replace(" ", "")  # Loại bỏ dấu cách
        code += f"\n# Bài {number}: \n# def {function_name}:\n# {function_name}\n"
    pyperclip.copy(code)
    print("Đã sao chép vào clipboard.")
create_def()