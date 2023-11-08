import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website
url = 'https://www.repubblica.it/'
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract article titles and links
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('h2').text
        link = article.find('a')['href']
        print(f"Title: {title}")
        print(f"Link: {link}")
