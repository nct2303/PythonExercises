import pandas as pd
import math

def Salary(salary):
    return salary * 90 / 100

dict_employees = {
    "ID" : [101, 102, 103, 104, 105, 106],
    "Name": ['An', 'Bình', 'Cường', 'Dương', None, 'Hạnh'],
    "Age": [25, None, 30, 22, 28, 35],
    "Department":  ['HR', 'IT', 'IT', 'Finance', 'HR', None],
    "Salary":  [700, 800, 750, None, 710, 770]
}

dict_departments = {
    "Department": ['HR', 'IT', 'Finance', 'Marketing'],
    'Manager': ['Trang', 'Khoa', 'Minh', 'Lan']
}

df_employees = pd.DataFrame(data = dict_employees)
df_departments = pd.DataFrame(data = dict_departments)

# 1. Kiểm tra các ô dữ liệu bị thiếu trong bảng Nhân viên.
print("\n1.")
print(df_employees.isnull())

# 2. Xoá các dòng trong bảng Nhân viên nếu dòng đó có hơn 2 giá trị bị thiếu.
print("\n2.")
print(df_employees.dropna())

# 3. Điền giá trị cho các ô bị thiếu:
new_values = {
    "Name" : "Chưa rõ",
    "Age" : (25 + 30 + 22 + 28 + 35)/6,
    "Salary" : 750,
    "Department" : "Unknow"
}
df_new_employees = df_employees.fillna(value=new_values)
print("\n3.")
print(df_new_employees)

# 4. Chuyển kiểu dữ liệu của Age và Salary sang int.
df_new_employees['Age'] = df_new_employees['Age'].astype(int)
df_new_employees['Salary'] = df_new_employees['Salary'].astype(int)
print("\n4.")
print(df_new_employees)

# 5. Tạo cột mới Salary_after_tax: giá trị sẽ là cột Salary -10% thuế
df_new_employees['Salary_after_tax'] = df_new_employees['Salary'].apply(Salary)
print("\n5.")
print(df_new_employees)

# 6. Lọc ra các nhân viên thuộc phòng IT và có tuổi lớn hơn 25.
print("\n6.")
print(df_new_employees.loc[(df_new_employees['Age'] > 25) & (df_new_employees['Department'] == 'IT')])

# 7. Sắp xếp bảng nhân viên theo Salary_after_tax giảm dần.
print("\n7.")
print(df_new_employees['Salary_after_tax'].sort_values(ascending=False))

# 8. Nhóm nhân viên theo Department và tính mức lương trung bình cho từng phòng ban.
print("\n8.")
print(df_new_employees.groupby("Department")["Salary"].mean().sort_values(ascending=False))

# 9. Dùng merge() để nối bảng nhân viên với bảng quản lý phòng ban theo cột Department để biết ai là Manager của từng nhân viên.
print("\n9.")
print(df_new_employees.merge(df_departments, on = 'Department', how='left'))

# 10. Tạo bảng Nhân viên Mới gồm 2 nhân viên mới và dùng concat() để thêm họ vào bảng Nhân viên.
dict_new_employees = {
    "ID" : [103, 104],
    "Name": ['Tú', 'Thắng'],
    "Age": [22, 23],
    "Department":  ['BA', 'PM'],
    "Salary":  [740, 780]
}
print("\n10. ")
df_add_new_employees = pd.DataFrame(data = dict_new_employees)
df_list_employees = pd.concat([df_new_employees, df_add_new_employees], ignore_index=True)
print(df_list_employees)