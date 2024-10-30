import requests
from bs4 import BeautifulSoup
import trafilatura
import pandas as pd
import time
import json

# AP section URLs for world and US elections
section_urls = [
    "https://apnews.com/hub/election-2024",
    "https://apnews.com/politics",
    "https://apnews.com/hub/congress"
]

# Initialize list for all article links
article_links = set()  # Using a set to avoid duplicates

# Loop through each section and collect article URLs
for section_url in section_urls:
    response = requests.get(section_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for link in soup.find_all('a', href=True):
        url = link['href']
        # Filter for article links by year and ensure full URL format
        if 'article' in url:
            full_url = f"https://www.apnews.com{url}" if url.startswith('/') else url
            article_links.add(full_url)

# Limit to only 100 articles for consistency with other sources
article_links = list(article_links)[:100]

# Storage for article content
articles = []

# Loop through each unique article URL to extract content
for article_url in article_links:
    print(f"Scraping {article_url}")
    try:
        downloaded = trafilatura.fetch_url(article_url)
        if downloaded:
            # Extract content with metadata in JSON format
            content = trafilatura.extract(downloaded, with_metadata=True, include_comments=False, output_format='json', favor_precision=True)
            if content:
                content_json = json.loads(content)
                articles.append({
                    'source': 'AP',                    # Source name
                    'title': content_json.get('title'),    # Title from metadata
                    'content': content_json.get('text'),   # Main content text
                    'date': content_json.get('date')       # Date if available
                })
    except Exception as e:
        print(f"Failed to scrape {article_url}: {e}")
    time.sleep(1)  # Be polite to the server with a delay

# Convert to DataFrame and save to CSV
df = pd.DataFrame(articles)
df.to_csv('ap_articles.csv', index=False)
print("Scraping complete. Saved to ap_articles.csv")
