from url_text import get_text
from finder import word_finder

word = "NoSQL"
url = "https://aws.amazon.com/tr/nosql/"
text = get_text(url)
print(text)
result = word_finder(word, text)
print(result)