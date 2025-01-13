import requests
from bs4 import BeautifulSoup

def fetch_lytics_docs():
    url = "https://docs.lytics.com/"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return ' '.join([p.get_text() for p in soup.find_all('p')])
