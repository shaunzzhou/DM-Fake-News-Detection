import trafilatura
import pandas as pd
import json

failed_urls = []
# Function to scrape a single news article with metadata, exclude comments
def scrape_article(url):
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            # Include metadata such as title, author, date; exclude comments
            content = trafilatura.extract(downloaded, only_with_metadata=True, include_comments=False, output_format='json')
            print(f"Extracted content for {url}: {content}")
            return content
        else:
            print(f"Failed to fetch content from: {url}")
            failed_urls.append(url)
            return None
    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")
        return None

# Function to scrape multiple articles, return a list of dictionaries
def scrape_all_articles(urls, source_name):
    articles = []
    for idx, url in enumerate(urls):
        print(f"Scraping {idx+1}/{len(urls)}: {url}")
        content = scrape_article(url)
        if content:
            print(f"Scraped content from {url}.")
            content_json = json.loads(content)  # Parse the JSON output from trafilatura
            # Adding source information and additional metadata to the article data
            article_data = {
                'source_name':source_name,
                'url': url,
                'title': content_json.get('title'), # Extract title from metadata
                'content': content_json.get('text')
            }
            print(f"Title: {article_data['title']}")
            articles.append(article_data)
        else:
            print(f"No valid content found for {url}.")
    return articles

# List of URLs to scrape for US news sites
# Unreliable sites
unreliable_sites = {
    'Breitbart': [
        'https://www.breitbart.com/the-media/2024/09/26/kamala-harris-taking-no-questions-bolts-from-podium-after-remarks-with-volodymyr-zelensky/',
        'https://www.breitbart.com/entertainment/2024/09/26/disney-bloodbath-latest-round-of-layoffs-hitting-hundreds-of-corporate-employees/',
        
    ],
    'The Gateway Pundit': [
        'https://www.thegatewaypundit.com/2024/09/kid-absolutely-bodies-kamala-harris-cnn-video/',
        'https://www.thegatewaypundit.com/2024/09/hes-shot-biden-randomly-starts-screaming-nowhere-claims/',
       
    ],
    'InfoWars': [
        'https://www.infowars.com/posts/boom-gop-texas-senator-ted-cruz-drops-crushing-ad-criticizing-democrat-opponent-allred',
        'https://www.infowars.com/posts/fbi-whistleblower-warns-americans-pray-stock-up-on-food-water-ammunition',
       
    ],
    'The Epoch Times': [
        'https://www.theepochtimes.com/us/new-york-city-mayor-adams-faces-pressure-after-federal-indictment-5730900?ea_src=frontpage&ea_cnt=a&ea_med=top-news-9-top-stories-0-title-0',
        'https://www.theepochtimes.com/health/inexpensive-infusion-helps-prevent-cerebral-palsy-in-babies-clinicians-encourage-global-uptake-5730914?ea_src=frontpage&ea_cnt=a&ea_med=top-news-13-top-stories-0-title-0',
       
    ],
    'Natural News': [
        'https://www.naturalnews.com/2024-09-20-urgent-alert-uv-laser-directed-energy-attack-alert-details.html',
        'https://www.naturalnews.com/2024-09-01-christian-churches-israel-mass-killing-palestinian-civilians-satan.html',
       
    ]
}

# Reputable sites
reputable_sites = {
    'Fox News': [
        'https://www.foxnews.com/politics/harris-heads-southern-border-looking-flip-script-immigration-criticisms',
        'https://www.foxnews.com/politics/multiple-people-ties-iran-indicted-relation-trump-campaign-hacking-plot-sources',
       
    ],
    'The Guardian': [
        'https://www.theguardian.com/world/2024/sep/27/lebanon-israel-hezbollah-ceasefire-hopes-fade-netanyahu',
        'https://www.theguardian.com/world/2024/sep/26/zelenskyy-biden-white-house',
       
    ],
    'CNN': [
        'https://edition.cnn.com/2024/09/27/middleeast/israel-pager-attack-hezbollah-lebanon-invs-intl/index.html',
        'https://edition.cnn.com/2024/09/26/asia/south-korea-deepfake-bill-passed-intl-hnk/index.html',
       
    ],
    'BBC News (US Edition)': [
        'https://www.bbc.com/news/articles/c7810y11dyjo',
        'https://www.bbc.com/news/articles/clylgv2dk3yo'
    ],
    'NPR': [
        'https://www.npr.org/2024/09/25/nx-s1-5111891/independent-third-party-candidates-swing-state-ballots',
        'https://www.npr.org/2024/09/26/nx-s1-5111886/pennsylvania-mail-in-ballot-lawsuit-2024-election',
       
    ]
}

# Scraping articles from all unreliable sites
scraped_articles = []
for source, urls in unreliable_sites.items():
    print(f"Scraping from {source}...")
    articles = scrape_all_articles(urls, source)
    scraped_articles.extend(articles)

# Scraping articles from all reputable sites
for source, urls in reputable_sites.items():
    print(f"Scraping from {source}...")
    articles = scrape_all_articles(urls, source)
    scraped_articles.extend(articles)

# Check if any articles were successfully scraped
if scraped_articles:
    # Create a DataFrame from the scraped data with the specified columns
    articles_df = pd.DataFrame(scraped_articles, columns=['source_name','url', 'title', 'content'])

    # Save the DataFrame to a CSV file
    articles_df.to_csv('scraped_articles.csv', index=False)

    # Display the DataFrame to verify the content
    print(articles_df.head())
    
    #Shows which urls we failed to scrape from
    print(f"Failed to scrape content from the following URLs: {failed_urls}")
else:
    print("No articles were scraped successfully.")