from bs4 import BeautifulSoup
import requests


def word_finder(word, url):
    word = word.lower()
    header = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "lxml")
    text = soup.text.lower()

    dict = {}
    count = 0
    cursor = 0
    while True:

        if text.find(word, cursor) != -1:
            count += 1
            start = text.find(word, cursor)
            finish = start + len(word)
            dict.update({count: {"Start": start, "Finish": finish}})
            cursor = finish
        else:
            print(count)
            break

    return dict

"""
word = "NoSQL"
url = "https://aws.amazon.com/tr/nosql/"
print(word_finder(word, url))
"""