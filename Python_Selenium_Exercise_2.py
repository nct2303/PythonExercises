from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Cấu hình trình duyệt
driver = webdriver.Chrome()
driver.get("https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep")
time.sleep(5)  # Chờ trang tải xong

# Khởi tạo writer để ghi nhiều sheet
writer = pd.ExcelWriter("doanh_nghiep_mst.xlsx", engine='openpyxl')

page = 1

while True:
    print(f"Đang xử lý trang {page}...")

    time.sleep(2)  # Chờ load dữ liệu trang

    rows = driver.find_elements(By.CSS_SELECTOR, "div.item")

    if not rows:
        print("Không tìm thấy dữ liệu trên trang này. Kết thúc.")
        break

    data = []

    for row in rows:
        try:
            name = row.find_element(By.CSS_SELECTOR, "h3 a").text.strip()
            mst = row.find_element(By.XPATH, ".//div[contains(text(),'Mã số thuế')]").text.split(":")[1].strip()
            ngay_cap = row.find_element(By.XPATH, ".//div[contains(text(),'Ngày cấp')]").text.split(":")[1].strip()

            data.append({
                "Tên doanh nghiệp": name,
                "Mã số thuế": mst,
                "Ngày cấp": ngay_cap
            })
        except:
            continue

    # Ghi vào sheet tương ứng
    df = pd.DataFrame(data)
    df.to_excel(writer, sheet_name=f"Trang_{page}", index=False)

    # Tìm nút "Trang tiếp" (dấu →)
    try:
        next_btn = driver.find_element(By.XPATH, "//a[@rel='next']")
        if 'disabled' in next_btn.get_attribute("class"):
            print("Đã đến trang cuối.")
            break
        next_btn.click()
        page += 1
    except:
        print("Không tìm thấy nút trang tiếp. Kết thúc.")
        break

# Lưu file Excel
writer.close()
driver.quit()
print("Đã lưu dữ liệu thành công vào doanh_nghiep_mst.xlsx")
