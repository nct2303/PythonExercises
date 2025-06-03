import pandas as pd

# Hàm đánh giá điểm để trả về 'True' hoặc 'False'
def evaluate_score(score):
    if score >= 5:
        return 'True'
    return 'False'

# Dữ liệu mẫu
data = {
    "Name": ["Thien", "Hung", "Linh", "Huong", "Dung", "Bao", "Hinh", "Tien", "Anh", "Ngoc"],
    "Age": [22, 22, 21, 23, 22, 22, 20, 21, 22, 22],
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female"],
    "Score": [5, 4, 6, 8, 3, 5, 2, 4, 1, 9]
}

# Tạo DataFrame với index từ 1 đến 10
df = pd.DataFrame(data=data, index=range(1, 11))

# In toàn bộ dữ liệu của bảng
print("In toàn bộ dữ liệu của bảng:\n")
print(df)

# In 3 dòng đầu tiên
print("In 3 dòng đầu tiên:\n")
print(df.head(3))

# Lấy dữ liệu theo index và cột cụ thể
print("\nTheo index=2 và cột Name:")
print(df.loc[2, 'Name'])

print("\nTheo index=10 và cột Age:")
print(df.loc[10, 'Age'])

# In 2 cột Name và Score
print("\nCác cột Name và Score:")
print(df.loc[:, ['Name', 'Score']])

# Thêm cột Pass dựa trên điều kiện của hàm evaluate_score
print("\nThêm một cột tên Pass:")
df['Pass'] = df['Score'].apply(evaluate_score)
print(df)

# Sắp xếp DataFrame giảm dần theo cột Score
print("\nSắp xếp giảm dần theo Score:")
print(df.sort_values(by='Score', ascending=False))
