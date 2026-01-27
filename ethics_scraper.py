import requests
import json
import time
print("Script started...")
api_key = "417613e121574b3cb2d96ecda3e412a9"
url = "https://newsapi.org/v2/everything"
search_queries = [
    'ethics'
]
parameters = {
    'apiKey': api_key,
    'language': 'en',
    'domains': (
        'reuters.com,theguardian.com,wired.com,theverge.com,'
        'sciencedaily.com,technologyreview.com,theconversation.com,'
        'nature.com,ox.ac.uk,harvard.edu,mit.edu,cam.ac.uk,yale.edu, project-syndicate.org,'
        'stanford.edu,brookings.edu,hastingscenter.org,iea.org.uk,'
        'bioethicstoday.org,thehastingscenter.org,kennedyinstitute.georgetown.edu,'
        'nuffieldbioethics.org,bioethics.jhu.edu,onlinelibrary.wiley.com,'
        'jme.bmj.com,cjb-rcb.ca,bmcmedethics.biomedcentral.com,coe.int,'
        'euobserver.com,euractiv.com,fra.europa.eu,europa.eu,bioethics.com'
        'apnews.com, nuffieldbioethics.org,'
    ),
    'from': '2025-11-01',
    'sortBy': 'relevancy',
    'pageSize': 100
}
for query in search_queries:
    print(f"--- Now searching for: '{query}' ---")
    parameters['q'] = query
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        try:
            data = response.json()
            if 'articles' in data:
                print(f"Found {len(data['articles'])} articles. Displaying now...")
                for article in data['articles']:
                    title = article.get('title', 'No title available')
                    author = article.get('author', 'No author available')
                    description = article.get('description', 'No description available')
                    url = article.get('url', 'No URL available')
                    print(f"Title: {title}")
                    print(f"Author: {author}")
                    print(f"Description: {description}")
                    print(f"URL: {url}")
                    print("-" * 50)
            else:
                print("No articles found in the response for this query.")
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print(f"Server response text was: {response.text}")
    else:
        print(f"Error: {response.status_code}")
        print(f"Server response text: {response.text}")
    time.sleep(5)
print("--- All searches complete. ---")
