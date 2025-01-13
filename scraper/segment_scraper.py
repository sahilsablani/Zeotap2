import requests
from bs4 import BeautifulSoup

def fetch_segment_docs():
    url = "https://segment.com/docs/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return ' '.join([p.get_text() for p in soup.find_all('p')])
