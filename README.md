# 🛒 E-commerce Price & Review Scraper (SauceDemo)

This is a Python-based web scraper that logs into [saucedemo.com](https://www.saucedemo.com), scrapes product data from the inventory page, and saves the results into a `products.csv` file.

## ✅ Features

- Logs in with username and password
- Uses `Selenium` for JavaScript-powered login
- Scrapes product name, price, and description
- Saves all data into a `CSV` file
- Headless mode supported (optional)

---

## 🧰 Requirements

Make sure you have the following installed:

- Python 3.8+
- Google Chrome (installed)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (handled automatically by `webdriver-manager`)

### Install dependencies

```bash
pip install selenium webdriver-manager
