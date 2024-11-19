import trafilatura
import pandas as pd

# Function to scrape a single news article
def scrape_article(url):
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            #include metadata such as title, author, date, etc., exclude comments
            content = trafilatura.extract(downloaded, include_metadata=True, include_comments=False)
            return content
        else:
            print(f"Failed to fetch content from: {url}")
            return None
    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")
        return None

# Function to scrape multiple articles, return a list of dictionaries
def scrape_all_articles(urls):
    articles = []
    for idx, url in enumerate(urls):
        print(f"Scraping {idx+1}/{len(urls)}: {url}")
        content = scrape_article(url)
        if content:
            print(f"Scraped content from {url}.")
            articles.append(content)
        else:
            print(f"No valid content found for {url}.")
    return articles

# tentative plan is to use 10 urls from 5 different news websites
news_urls = [
    'https://www.theguardian.com/us-news/2024/sep/21/saginaw-michigan-swing-state-trump-harris-election',
    'https://edition.cnn.com/world/live-news/israel-lebanon-attacks-09-21-24/index.html',
    ]

# Scrape articles and store them in a list of dictionaries
scraped_articles = scrape_all_articles(news_urls)

# Check if any articles were successfully scraped
if scraped_articles:
    # Create a DataFrame from the scraped data
    articles_df = pd.DataFrame(scraped_articles)

    # Save the DataFrame to a CSV file
    articles_df.to_csv('scraped_articles.csv', index=False)

    # Display the DataFrame to verify the content
    print(articles_df.head())
else:
    print("No articles were scraped successfully.")