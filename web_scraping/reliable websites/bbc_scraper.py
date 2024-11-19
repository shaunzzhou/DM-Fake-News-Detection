import requests
from bs4 import BeautifulSoup
import trafilatura
import pandas as pd
import time
import json

# BBC section URL for US elections
section_urls = ["https://www.bbc.com/news/topics/cj3ergr8209t", # US elections
                "https://www.bbc.com/news/topics/c34k011x7rrt", # Kamala Harris
                "https://www.bbc.com/news/topics/cp7r8vgl2lgt", # Donald Trump
                "https://www.bbc.com/news/topics/c79wd85wg8et", # JD Vance
                "https://www.bbc.com/news/topics/cwywpe90nnyt", # Tim Walz
                "https://www.bbc.com/news/politics", # Politics
                "https://www.bbc.com/news/us-canada" # US & Canada
                ] 

# Initialize set for article links to avoid duplicates
article_links = set()

# Collect initial article URLs from the section page
for section_url in section_urls:
    response = requests.get(section_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article links
    for link in soup.find_all('a', href=True):
        url = link['href']
        # Debugging: Print out each link to check what's being found
        print("Found link:", url)
        
        # Filter for article links that have "/world/us/" in the URL and are recent (contain a date format)
        if '/news/articles/' in url:
            full_url = f"https://www.bbc.com{url}" if url.startswith('/') else url
            article_links.add(full_url)

# Check if any article links were found
print("Total articles found:", len(article_links))
if not article_links:
    print("No articles found. Adjust your filters or check the section URL.")
else:
    # Limit to at most 200 articles to avoid long runtimes
    article_links = list(article_links)[:200]

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
                        'source': 'BBC',                    # Source name
                        'title': content_json.get('title'),    # Title from metadata
                        'content': content_json.get('text'),   # Main content text
                        'date': content_json.get('date')       # Date if available
                    })
        except Exception as e:
            print(f"Failed to scrape {article_url}: {e}")
        time.sleep(1)  # Be polite to the server with a delay

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(articles)
    df.to_csv('bbc_articles.csv', index=False)
    print("Scraping complete. Saved to bbc_articles.csv")
