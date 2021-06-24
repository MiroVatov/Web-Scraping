from bs4 import BeautifulSoup
import requests
import csv

# get the response in the form of html
wikiurl = "https://en.wikipedia.org/wiki/Lionel_Messi"
response = requests.get(wikiurl)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')


club_heading = soup.find(id='Club_2')
club_honors_lists = club_heading.find_next('ul')

print(club_heading.text + '\n')
print(club_honors_lists.text + '\n')


international_heading = soup.find(id='International_2')
international_honors_list = international_heading.find_next('ul')
international_honors2 = international_honors_list.find_next('ul')
international_honors = international_honors_list.text + international_honors2.text
print(international_heading.text + '\n')
print(international_honors_list.text + '\n' + international_honors2.text + '\n')

individual_heading = soup.find(id='Individual')
individual_honors_list = individual_heading.find_next('ul')
print(individual_heading.text + '\n')
print(individual_honors_list.text + '\n')

see_also_heading = soup.find(id='See_also')
see_also_details = see_also_heading.find_next('ul')
see_also_details2 = see_also_details.find_next('ul')
print(see_also_heading.text + '\n')
print(see_also_details2.text + '\n')

messi_honours_data = [(club_heading, club_honors_lists), (international_heading, international_honors), (individual_heading, individual_honors_list), (see_also_heading, see_also_details2)]

csv_file = open('messi_honours.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Header', 'Honours'])


for header, lst in messi_honours_data:
    Honours_lst = lst
    if not isinstance(lst, str):
        Honours_lst = lst.text
    csv_writer.writerow([header.text, Honours_lst])

csv_file.close()