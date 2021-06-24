from bs4 import BeautifulSoup  # library to parse HTML documents
import requests  # library to handle requests
import pandas as pd  # library for data analysis
import csv

# get the response in the form of html
wikiurl = "https://en.wikipedia.org/wiki/Lionel_Messi"
table_class = "wikitable"
response = requests.get(wikiurl)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
messitable = soup.find('table', {'class': "wikitable"})

df = pd.read_html(str(messitable))
# convert list to dataframe
df = pd.DataFrame(df[0])

print(df)

csv_file = open('messi_table_stats.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Club', 'Season', 'Division', 'LeagueApps', 'LeagueGoals', 'CopDelReyApps', 'CopDelReyGoals', 'ChampionsLeagueApps', 'ChampionsLeagueGoals,', 'OtherApps', 'OtherGoals', 'TotalApps', 'TotalGoals'])


for series in df.iterrows():

    Club = series[1].Club.Club

    Season = series[1].Season.Season

    Division = series[1].League.Division

    LeagueApps = series[1].League.Apps

    LeagueGoals = series[1].League.Goals

    CopaDelReyApps = series[1].T[5][0]

    CopaDelReyGoals = series[1].T[6][0]

    ChampionsLeagueApps = series[1].T[7][0]

    ChampionsLeagueGoals = series[1].T[8][0]

    OtherApps = series[1].Other.Apps

    OtherGoals = series[1].Other.Goals

    TotalApps = series[1].Total.Apps

    TotalGoals = series[1].Total.Goals

    csv_writer.writerow([Club, Season, Division, LeagueApps, LeagueGoals, CopaDelReyApps, CopaDelReyGoals, ChampionsLeagueApps, ChampionsLeagueGoals, OtherApps, OtherGoals, TotalApps, TotalGoals])


csv_file.close()