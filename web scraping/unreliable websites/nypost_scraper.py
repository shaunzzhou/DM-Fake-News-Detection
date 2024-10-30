import requests
from bs4 import BeautifulSoup
import trafilatura
import pandas as pd
import time
import json

# New York Post politics section URL
section_url = ["https://nypost.com/politics/",
                "https://nypost.com/politics/page/2/",
               ]

# Initialize a set to store unique article links
article_links = set()

# Request the main section page and parse for article links
response = requests.get(section_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Collect article links on the main politics page
for link in soup.find_all('a', href=True):
    url = link['href']
    if "/2024/" in url or "/2023/" in url:  # Filter for recent articles
        full_url = f"https://nypost.com{url}" if url.startswith('/') else url
        article_links.add(full_url)

# Limit to the first 100 articles for consistency with other sources
article_links = list(article_links)[:100]
print(f"Number of unique article links collected: {len(article_links)}")

# Storage for article content
articles = []

# Loop through each article URL to extract content
for article_url in article_links:
    print(f"Scraping {article_url}")
    try:
        # Fetch and extract article content
        downloaded = trafilatura.fetch_url(article_url)
        if downloaded:
            content = trafilatura.extract(downloaded, with_metadata=True, include_comments=False, output_format='json', favor_precision=True)
            if content:
                content_json = json.loads(content)
                articles.append({
                    'source': 'New York Post',               # Source name
                    'title': content_json.get('title'),      # Title from metadata
                    'content': content_json.get('text'),     # Main content text
                    'date': content_json.get('date')         # Date if available
                })
    except Exception as e:
        print(f"Failed to scrape {article_url}: {e}")
    time.sleep(1)  # Be polite to the server with a delay

# Convert to DataFrame and save to CSV
df = pd.DataFrame(articles)
df.to_csv('nypost_articles.csv', index=False)
print("Scraping complete. Saved to nypost_articles.csv")
