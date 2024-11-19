import requests
from bs4 import BeautifulSoup
import trafilatura
import pandas as pd
import time
import json

# AP section URLs for world and US elections
section_urls = [
    "https://npr.org/sections/elections/",
    "https://npr.org/sections/politics",
    "https://npr.org/sections/law/",
    "https://npr.org/tags/134949364/donald-trump",
    "https://npr.org/tags/619450070/kamala-harris"
]

# Initialize list for all article links
article_links = set()  # Using a set to avoid duplicates

# Loop through each section and collect article URLs
for section_url in section_urls:
    response = requests.get(section_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for link in soup.find_all('a', href=True):
        url = link['href']
        print("Found link:", url)
        # Filter for article links by year and ensure full URL format
        if '/2024' in url and 'mp3' not in url:
            full_url = f"https://www.npr.org{url}" if url.startswith('/') else url
            article_links.add(full_url)

# Limit to at most 200 articles to avoid long runtimes
article_links = list(article_links)[:200]
print(f"Number of unique article links collected: {len(article_links)}")

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
                    'source': 'NPR',                    # Source name
                    'title': content_json.get('title'),    # Title from metadata
                    'content': content_json.get('text'),   # Main content text
                    'date': content_json.get('date')       # Date if available
                })
    except Exception as e:
        print(f"Failed to scrape {article_url}: {e}")
    time.sleep(1)  # Be polite to the server with a delay

# Convert to DataFrame and save to CSV
df = pd.DataFrame(articles)
df.to_csv('npr_articles.csv', index=False)
print("Scraping complete. Saved to npr_articles.csv")