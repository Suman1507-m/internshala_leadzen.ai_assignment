import requests
from bs4 import BeautifulSoup

# Number of pages to scrape
num_pages = 20

# Base URL for the product listing
base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"

# List to store scraped data
products = []

# Iterate over the specified number of pages
for page in range(1, num_pages + 1):
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product containers on the page
    product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    # Extract required information from each product container
    for container in product_containers:
        # Product URL
        product_url = container.find('a', {'class': 'a-link-normal'}).get('href')
        
        # Product Name
        product_name = container.find('span', {'class': 'a-size-medium'}).text.strip()
        
        # Product Price
        product_price = container.find('span', {'class': 'a-price-whole'}).text.strip()
        
        # Rating
        rating = container.find('span', {'class': 'a-icon-alt'}).text.strip()
        
        # Number of reviews
        num_reviews = container.find('span', {'class': 'a-size-base'}).text.strip()
        
        # Store the scraped data in a dictionary
        product_data = {
            'Product URL': product_url,
            'Product Name': product_name,
            'Product Price': product_price,
            'Rating': rating,
            'Number of Reviews': num_reviews
        }
        
        # Append the dictionary to the products list
        products.append(product_data)

# Print the scraped data
for product in products:
    print(product)
