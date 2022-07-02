from bs4 import BeautifulSoup
import requests

def get_text(url):

    header = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "lxml")
    text = soup.find('main').text

    return text