import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

#/////////////////////////////////
# Title: Reading and Writing to text files in Python
# Name: N/A
# Site Owner: Geeks for Geeks
# Date: August 28, 2023
# Code-Version: N/A
# Availability: https://www.geeksforgeeks.org/reading-writing-text-files-python/
# Modified: Yes
file1 = open("hockeydata.txt", 'w')

date = []
team = []
playerLeavingInjury = []
playerOnInjury = []
injury = []

number = 0
playerFirstName = []
playerLastName = []
lastOne = ""
firstTwo = ""
lastFive = ""
rows = []
cols = []
header = ""
player = []
years = []
page = 0
header = []
rows = []
#/////////////////////////////////
# Title: How to scrape tables with BeautifulSoup?
# Name: Dimitrije Stamenic
# Site Owner: ScrapFly
# Date: OCt. 24, 2022
# Code-Version: N/A
# Availability: https://scrapfly.io/blog/how-to-scrape-tables-with-beautifulsoup/
# Modified: Yes
url = "https://www.prosportstransactions.com/hockey/Search/SearchResults.php?Player=&Team=&BeginDate=2023-02-01&EndDate=2023-02-10&ILChkBx=yes&submit=Search&start={}"
response =requests.get(url.format(page))
soup=BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')
while (len(table.find_all('tr')) > 1):
    page +=25
    for i, row in enumerate(table.find_all('tr')):
        if i == 0:
            header = [el.text.strip() for el in row.find_all('td')]
        else:
            rows.append([el.text.strip() for el in row.find_all('td')])
    response =requests.get(url.format(page))
    soup=BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
file1.writelines("% s\n" % data for data in rows)
file1.close()
file1 = open("hockeydata.txt", 'r')

for line in file1:
    #/////////////////////////////////
    # Title: Split a String and get First or Last element in Python
    # Name: Borislav Hadzhiev
    # Site Owner: Bobbyhadz
    # Date: Feb. 19, 2023
    # Code-Version: N/A
    # Availability: https://bobbyhadz.com/blog/python-split-string-and-get-last-element
    # Modified: Yes
    date.append(line.split(',')[0])
    team.append(line.split(',')[1])
    playerLeavingInjury.append(line.split(',')[2])
    playerOnInjury.append(line.split(',')[3])
    if len(line.split(',')[4]) != 10:
        injury.append(line.split(',')[4])
    if (len(playerOnInjury[number]) == 3):
        playerLastName.append(playerLeavingInjury[number].split(" ")[3])
        playerFirstName.append(playerLeavingInjury[number].split(" ")[2])
    elif (len(playerLeavingInjury[number]) == 3):
        playerLastName.append(playerOnInjury[number].split(" ")[3])
        playerFirstName.append(playerOnInjury[number].split(" ")[2])
    number += 1
#/////////////////////////////////
# Title: How to Remove Quotes from Strings in Python
# Name: Dimitrije Stamenic
# Site Owner: StackAbuse
# Date: June 1, 2023
# Code-Version: N/A
# Availability: https://stackabuse.com/how-to-remove-quotes-from-string-in-python/
# Modified: Yes
playerLastName = [item.replace("'","") for item in playerLastName]
playerLastName = [item.replace('"','') for item in playerLastName]
playerFirstName = [item.replace("'","") for item in playerFirstName]
date = [item.replace("'","") for item in date]
date = [item.replace('[','') for item in date]
injury = [item.replace("'","") for item in injury]
team = [item.replace("'","") for item in team]
name = -1
for data in playerFirstName:
    print(data)
    lastOne = playerLastName[name][0].lower()
    firstTwo = playerFirstName[name][0].lower() + playerFirstName[name][1]
    lastFive = playerLastName[name][0 : 5].lower()
    url = "https://www.hockey-reference.com/players/" + lastOne + "/" + lastFive + firstTwo + "01.html"
    print(url)
    time.sleep(5)
    response =requests.get(url.format())
    soup=BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', id="stats_basic_plus_nhl")
    pageNumb = 2
    while (table is None and pageNumb < 10):
        url = "https://www.hockey-reference.com/players/" + lastOne + "/" + lastFive + firstTwo + "0" + str(pageNumb) + ".html"
        response =requests.get(url.format())
        soup=BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', id="stats_basic_plus_nhl")
        pageNumb += 1
    if table is not None:
        for i, row in enumerate(table.find_all('tr')):
            if i == 0 or i == 1:
                header = [el.text.strip() for el in row.find_all('th')]
            else:
                years = [el.text.strip() for el in row.find_all('th')]
                player = [el.text.strip() for el in row.find_all('td')]
                rows.append(years + player)
    if (len(rows)>0) and len(rows[0])==30:
        for e in rows:
            cols.append([playerFirstName[name], playerLastName[name], date[name], team[name], injury[name], e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13],e[14],e[15],
                e[16],e[17],e[18],e[19],e[20],e[21],e[22],e[23],e[24],e[25],e[26],e[27],e[28],e[29]])
    rows = []
    name +=1
#/////////////////////////////////////////
# Title: pandas.DataFrame.to_csv
# Name: N/A
# Site Owner: Pandas
# Date: N/A
# Code-Version: 2.1.3
# Availability: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
# Modified: Yes
df = pd.DataFrame(cols,columns=["Player First Name","Player Last Name","Date of Injury","Team When Injured","Injury Description", "Season","Age","Team","League",
                  "Games Played","Goals","Assists","Points","+/-","Penalties in Minutes","Even Strength Goals","Power Play Goals","Short Handed Goals",
                  "Game-Winning Goals","Even Strength Assists","Power Play Assists","Short-Handed Assists","Shots On Goals","Shooting Percentage","Total Shoot Assists",
                  "Time on Minutes","Average Time on Ice","Faceoff Wins","Faceoff Losses","Faceoff Percentage","Blocks","Hits","Takeaways","Giveaways","Awards"])
df.to_csv("playerData.csv")
file1.close()
print("finished")