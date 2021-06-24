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
messi_international_table = soup.findAll('table', {'class': "wikitable"})

df = pd.read_html(str(messi_international_table))

# convert list to dataframe
df = pd.DataFrame(df[1])

print(df)

csv_file = open('messi_international_table_stats.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Team', 'Year', 'CompetitiveApps', 'CompetitiveGoals', 'FriendlyApps', 'FriendlyGoals', 'TotalApps', 'TotalGoals'])


def format_team_length(team):
    if ' ' in team:
        team = team[:13]
        return team

    team = team[:9]
    return team


def format_competitive_apps(apps):
    digits = [int(d) for d in apps.split('[') if d.isdigit()]
    if digits:
        return digits[0]
    return '-'


for series in df.iterrows():
    try:
        Team = series[1].Team.Team
        Team = format_team_length(Team)
        Year = series[1].Year.Year
        CompetitiveApps = series[1].Competitive.Apps
        CompetitiveApps = format_competitive_apps(CompetitiveApps)
        CompetitiveGoals = series[1].Competitive.Goals
        FriendlyApps = series[1].Friendly.Apps
        FriendlyGoals = series[1].Friendly.Goals
        TotalApps = series[1].Total.Apps
        TotalGoals = series[1].Total.Goals
        csv_writer.writerow(
            [Team, Year, CompetitiveApps, CompetitiveGoals, FriendlyApps, FriendlyGoals, TotalApps, TotalGoals])
    except UnicodeEncodeError:
        continue


csv_file.close()