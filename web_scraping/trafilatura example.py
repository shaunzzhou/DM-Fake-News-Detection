import trafilatura

from trafilatura import fetch_url, extract

# Use one url to test web scraper
url = 'https://www.infowars.com/posts/ice-arrests-another-suspected-sex-predator-on-loose-on-nantucket-island'

downloaded = fetch_url(url)

# Check if the content was successfully downloaded
if downloaded:
    # Extract the main text content from the downloaded HTML
    result = extract(downloaded,with_metadata=True)
    print(result)
else:
    print("Failed to fetch the content from the URL.")




