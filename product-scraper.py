from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

def login_and_scrape(username, password):
    options = Options()
    options.add_argument("--headless")  # comment this out if you want to see browser
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    products_data = []

    try:
        driver.get("https://www.saucedemo.com/")

        # Login
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Scrape products
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        for i, product in enumerate(products, 1):
            title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            desc = product.find_element(By.CLASS_NAME, "inventory_item_desc").text

            # print(f"{i}. {title} | {price} | {desc}")

            products_data.append({
                "title": title,
                "price": price,
                "description": desc
            })

    finally:
        driver.quit()

    return products_data

def save_to_csv(data, filename="products.csv"):
    """Save scraped product data to a CSV file."""
    with open(filename, mode="w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["title", "price", "description"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"✅ Data saved to {filename}")

# --- RUN SCRIPT ---
if __name__ == "__main__":
    username = "standard_user"
    password = "secret_sauce"

    scraped_data = login_and_scrape(username, password)
    save_to_csv(scraped_data)
