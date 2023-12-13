from bs4 import BeautifulSoup
import requests

# URL to scrape
url = "https://deetsdigital.com"

# Make an HTTP GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and print all the links on the page
    links = soup.find_all("a")
    for link in links:
        print("Link:", link.get("href"))
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
