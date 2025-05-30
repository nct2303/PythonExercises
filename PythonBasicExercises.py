#Viết chương trình đổi các từ ở đầu câu sang chữ hoa và những từ không phải đầu câu sang chữ thường.
def convert_text(my_string):
    sentences = my_string.split('.')
    result_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence == '':
            continue
        sentence = sentence.lower()
        sentence = sentence[0].upper() + sentence[1:]
        result_sentences.append(sentence)

    result = '. '.join(result_sentences) + '.'
    return result

#Viết chương trình đảo ngược thứ tự các từ có trong chuỗi.
def reverse_text(my_string):
    words = my_string.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

#Viết chương trình tìm kiếm ký tự xuất hiện nhiều nhất trong chuỗi.
def most_frequent_char(my_string):
    my_string = my_string.replace(" ", "")

    char_count = {}
    for char in my_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    most_char = max(char_count, key=char_count.get)
    max_count = char_count[most_char]
    return most_char, max_count

# 4. Viết chương trình nhập một chuỗi bất kỳ, liệt kê số lần xuất hiện của mỗi ký tự.
def count_characters(my_string):
    char_count = {}
    for char in my_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# 5. Viết hàm kiểm tra xem trong chuỗi có ký tự số hay không. Nếu có, tách các số đó ra thành một mảng riêng.
def extract_digits(my_string):
    digits = []
    for char in my_string:
        if char.isdigit():
            digits.append(char)
    return digits

# 6. Viết hàm cắt chuỗi họ tên thành chuỗi họ lót và chuỗi tên.
def split_full_name(full_name):
    parts = full_name.strip().split()
    if len(parts) < 2:
        return '', full_name
    middle_name = ' '.join(parts[:-1])
    last_name = parts[-1]
    return middle_name, last_name

# 7. Viết chương trình chuyển ký tự đầu tiên của mỗi từ trong chuỗi thành chữ in hoa.
def capitalize_first_letters(my_string):
    words = my_string.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result

# 8. Viết chương trình đổi chữ xen kẽ: một chữ hoa và một chữ thường.
def alternate_upper_lower(my_string):
    result = ''
    for i, char in enumerate(my_string):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

# 9. Viết chương trình nhập vào một chuỗi ký tự, kiểm tra xem chuỗi đó có đối xứng không.
def is_palindrome(my_string):
    clean_string = my_string.replace(' ', '').lower()
    return clean_string == clean_string[::-1]

# 10. Viết chương trình nhập vào một số có 3 chữ số, xuất ra dòng chữ mô tả giá trị con số đó.
def number_to_vietnamese_words(number):
    units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    num_str = str(number)
    if len(num_str) != 3 or not num_str.isdigit():
        return "Invalid number"

    hundred = int(num_str[0])
    ten = int(num_str[1])
    unit = int(num_str[2])

    result = f"{units[hundred]} trăm"
    if ten == 0 and unit != 0:
        result += " lẻ"
    elif ten != 0:
        result += f" {tens[ten]}"
    if unit != 0:
        if unit == 5 and ten != 0:
            result += " lăm"
        else:
            result += f" {units[unit]}"
    return result.strip()

