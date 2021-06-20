from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

# print(soup.prettify())

for article in soup.findAll('article'):
    headline = article.h2.a.text
    print(f"Headline: {headline}")

    summary = article.find('div', class_='entry-content')
    summary = summary.p.text
    print(f"Summary: {summary}")

    try:
        embedded_video = article.find('iframe', class_='youtube-player')
        vid_src = embedded_video['src']
        print(f"Video source:  {vid_src}")

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        youtube_link = f'https://youtube.com/watch?v={vid_id}'
        print(f"Youtube link: {youtube_link}")
        print()

        csv_writer.writerow([headline, summary, youtube_link])

    except TypeError:
        print('\n' + "--------------The above article does not have video link embedded----------------" + '\n')

        csv_writer.writerow([headline, summary])

csv_file.close()

