import requests
from bs4 import BeautifulSoup

# Use cleaner URL
url = "https://www.amazon.in/dp/B0F2FQKBK2"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

# Get product title
title = soup.find(id="productTitle")
if title:
    print("Product:", title.get_text(strip=True))
else:
    print("Title not found")

# Get product price
price = soup.find('span', {'class': 'a-price-whole'})
if price:
    print("Price:", price.get_text(strip=True))
    
    # Fix: Get the text from price element first
    price_text = price.get_text(strip=True)  # This gets the actual text like "899"
    price_clean = price_text.replace(',', '')  # Remove commas: "899"
    current_price = int(float(price_clean))    # Convert to int: 899
    
    target_price = 50000  # Set your expected price
    
    if current_price < target_price:
        print("💸 Price dropped! Buy now.")
    else:
        print("📈 Still expensive. Wait.")
        
else:
    print("Price not found")
