import requests
from bs4 import BeautifulSoup

class EcommerceScraper:
    def __init__(self, base_url, headers=None):
        self.session = requests.Session()
        self.base_url = base_url
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

    def fetch_page(self, url):
        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch {url}, Status code: {response.status_code}")
            return None

    def parse_products(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        products = []

        # Example selectors (you must customize these for the target website)
        for product in soup.select(".product-item"):
            title = product.select_one(".product-title")
            price = product.select_one(".price")
            review = product.select_one(".review-rating")

            products.append({
                "title": title.text.strip() if title else "N/A",
                "price": price.text.strip() if price else "N/A",
                "review": review.text.strip() if review else "N/A",
            })

        return products

    def scrape(self, page_url):
        html = self.fetch_page(page_url)
        if html:
            products = self.parse_products(html)
            return products
        return []

# --- USAGE ---
if __name__ == "__main__":
    # Example site (change this to the actual product list page)
    url = "https://example.com/products"

    scraper = EcommerceScraper(base_url="https://example.com")
    products = scraper.scrape(url)

    for i, product in enumerate(products, 1):
        print(f"{i}. {product['title']} | {product['price']} | {product['review']}")
