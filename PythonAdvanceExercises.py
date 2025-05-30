import math
# Kiểm tra một số có phải là số chính phương hay không
def is_perfect_square(number):
    if number < 0:
        return False
    root = int(math.sqrt(number))
    return root * root == number

# Tìm các số chia hết cho 3 nhưng không phải số chính phương trong đoạn [firstNumber, secondNumber]
def find_numbers(firstNumber, secondNumber):
    result = []
    for i in range(firstNumber, secondNumber + 1):
        if i % 3 == 0 and not is_perfect_square(i):
            result.append(str(i))
    return ','.join(result)

# Kiểm tra dữ liệu đầu vào và in ra kết quả
def main():
    try:
        a = int(input("Nhập a (số nguyên): "))
        b = int(input("Nhập b (số nguyên, b > a): "))
        if a >= b:
            print("a phải nhỏ hơn b.")
            return
    except ValueError:
        print("Dữ liệu nhập không hợp lệ. Vui lòng nhập số nguyên.")
        return

    output = find_numbers(a, b)
    print(output)
