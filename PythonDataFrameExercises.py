import pandas as pd

def evaluate_score(score):
    if score >= 5:
        return 'True'
    return 'False'

dict = {
    "Name": ["Thien", "Hung", "Linh", "Huong", "Dung", "Bao", "Hinh", "Tien", "Anh", "Ngoc"],
    "Age": [22, 22, 21, 23, 22, 22, 20, 21, 22, 22],
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Male", "Male", "Male", "Male", "Female"],
    "Score": [5, 4, 6, 8, 3, 5, 2, 4, 1, 9]
}

df = pd.DataFrame(data=dict, index = range(1,11))
print("In 3 dòng đầu tiên: \n")
print(df.head(3))

print("\nTheo index=2 và cột Name:")
search_at_index_2 = df.loc[2, 'Name']
print(search_at_index_2)

print("\nTheo index=10 và cột Age:")
search_at_index_10 = df.loc[10, 'Age']
print(search_at_index_10)

print("\nCác cột Name và Score: ")
print(df.loc[:, ['Name', 'Score']])

print("\nThêm một cột tên Pass: ")
df['Pass'] = df['Score'].apply(evaluate_score)
print(df)

print("\nSắp xếp giảm dần theo Score: ")
print(df.sort_values(by='Score', ascending=False))