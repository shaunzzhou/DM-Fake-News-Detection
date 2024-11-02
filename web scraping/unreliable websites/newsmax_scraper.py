import requests
from bs4 import BeautifulSoup
import trafilatura
import pandas as pd
import time
import json
import random

# Section URLs for world and US elections
section_urls = [
    "https://www.newsmax.com/archives/politics/1/2024/10/"
]

# Initialize list for all article links
article_links = set()  # Using a set to avoid duplicates
keywords = ["election", "2024 election", "vote", "voting", "poll", "ballot", "candidate",
            "presidential", "Republican", "Democrat", "Biden", "Trump", "Kamala Harris", "GOP", "presidential race", 
            "campaign", "debate", "nomination", "swing state", "voter turnout", "electoral college"]

# Loop through each section and collect article URLs
for section_url in section_urls:
    # response = requests.get(section_url, headers=headers)
    response = requests.get(section_url)
    print(f"Fetching {section_url} - Status Code: {response.status_code}")
    if response.status_code != 200:
        print(f"Failed to retrieve {section_url}")
        continue  # Skip this URL if not successful
    
    soup = BeautifulSoup(response.content, 'html.parser')
    found_links = 0  # Counter to check if any links were found
    
    for link in soup.find_all('a', href=True):
        url = link['href']
        # Check for keyword in URL to filter election-related articles
        if any(keyword.lower() in url.lower() for keyword in keywords):
            # Ensure full URL format
            full_url = f"https://www.newsmax.com{url}" if url.startswith('/') else url
            article_links.add(full_url)
            found_links += 1
    
    print(f"Number of links found on {section_url}: {found_links}")

# Limit to at most 200 articles to avoid long runtimes
article_links = list(article_links)[:200]
print(f"Total unique article links collected: {len(article_links)}")

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
                    'source': 'News Max',
                    'title': content_json.get('title'),
                    'content': content_json.get('text'),
                    'date': content_json.get('date')
                })
    except Exception as e:
        print(f"Failed to scrape {article_url}: {e}")
    time.sleep(random.randint(2, 5))  # Be polite to the server with a delay

# Convert to DataFrame and save to CSV
df = pd.DataFrame(articles)
df.to_csv('newsmax_articles.csv', index=False)
print("Scraping complete. Saved to newsmax_articles.csv")
