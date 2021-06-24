import re

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 1)

wikiurl = 'https://en.wikipedia.org/wiki/List_of_American_comedy_films'
print('Fetching main wiki article: %s' % wikiurl + '\n')

# get the response in the form of html
response = requests.get(wikiurl)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
print('Done. Extracting table links..' + '\n')

csv_file_movie_names = open('comedy_movies.csv', 'w')
csv_file_movie_links = open('comedy_movies_links.csv', 'w')

csv_writer_movie_names = csv.writer(csv_file_movie_names)
csv_writer_movie_names.writerow(['Title', 'Name', 'Link'])

links_content = {}
links_dict = {}


for link in soup.findAll('a', attrs={'href': re.compile('^/wiki/')}):
    try:
        links_content[link.text] = link.attrs['title']
        links_dict[link.text] = link.attrs['href']
        csv_writer_movie_names.writerow([link.text, link.attrs['title'], link.attrs['href']])

    except (KeyError, UnicodeEncodeError):
        continue

csv_file_movie_names.close()
csv_file_movie_links.close()

print('Done extracting links. About to fetch: %s links..' % len(links_content) + '\n')


