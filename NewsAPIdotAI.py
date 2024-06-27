import requests
import json

def fetch_headlines_for_keywords(api_key, keywords, max_articles=100):
    url = "http://eventregistry.org/api/v1/article/getArticles"
    headlines_by_keyword = {}

    for keyword in keywords:
        params = {
            'apiKey': api_key,
            'action': 'getArticles',
            'keyword': keyword,
            'lang': 'eng',
            'resultType': 'articles',
            'includeArticleTitle': 'true',
            'includeArticleBody': 'false',  # Exclude article bodies to focus on titles
            'includeArticleCategories': 'false',
            'includeArticleLocation': 'false',
            'includeArticleImage': 'false',
            'maxItems': max_articles  # Control the number of articles to fetch
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            headlines = [article['title'] for article in data.get('articles', {}).get('results', [])]
            headlines_by_keyword[keyword] = headlines
        else:
            headlines_by_keyword[keyword] = f"Error {response.status_code}: {response.text}"

    return headlines_by_keyword

# Replace 'YOUR_API_KEY' with your actual Event Registry API key
api_key = '8d80a266-cad3-4e80-a67a-f148a79c3b78'
keywords = ['technology', 'health', 'sports', 'politics']  # Add more keywords as needed
max_articles = 150  # Set the number of articles you want per keyword
headlines_by_keywords = fetch_headlines_for_keywords(api_key, keywords, max_articles)

# Print headlines organized by keyword
for keyword, headlines in headlines_by_keywords.items():
    print(f"Headlines for {keyword}:")
    for headline in headlines:
        print(f"- {headline}")
    print("\n")
