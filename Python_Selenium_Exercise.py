from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

usernames = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user"
]
password = "secret_sauce"

driver = webdriver.Chrome()
data = []

for username in usernames:
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    if "inventory" in driver.current_url:
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            data.append({
                "Username": username,
                "Product Name": name,
                "Price": price
            })

        # Logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)
    else:
        print(f"Không đăng nhập được với {username}")

df = pd.DataFrame(data)
df.to_excel("saucedemo_products.xlsx", index=False)

driver.quit()
