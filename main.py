from url_text import get_text
from finder import word_finder

word = "NoSQL"
url = "https://aws.amazon.com/tr/nosql/"

result = word_finder(word, get_text(url))
print(result)