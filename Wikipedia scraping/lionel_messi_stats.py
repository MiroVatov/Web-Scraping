from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://en.wikipedia.org/wiki/Lionel_Messi').text

soup = BeautifulSoup(source, 'lxml')

for data in soup.findAll('li'):
    try:
        main_articles_references = data.contents[0].attrs["href"]
        # article = main_articles_references.href.str
        print(main_articles_references.replace('#', ''))
        print()

    except (KeyError, AttributeError):
        print(data.text)






