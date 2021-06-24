from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 1)

# get the response in the form of html
wikiurl = "https://en.wikipedia.org/wiki/List_of_science_fiction_films_of_the_1970s"
response = requests.get(wikiurl)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
movies_table = soup.find('table', {'class': "wikitable"})
df = pd.read_html(str(movies_table))

# convert list to dataframe
df = pd.DataFrame(df[0])
print(df)

csv_file = open('sci_fi_movies_from_70s.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Director', 'Cast', 'Country', 'Subgenre'])

for series in df.itertuples():
    if series.Index <= 1:
        continue
    title = series[1]
    director = series[2]
    cast = series[3]
    country = series[4]
    subgenre = series[5]
    try:
        csv_writer.writerow([title, director, cast, country, subgenre])
    except UnicodeEncodeError:
        continue

csv_file.close()
