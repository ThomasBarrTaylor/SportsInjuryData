import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

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
injuryDataset = []
number = 0
playerFirstName = []
playerLastName = []

totalTeam = []
totalInjury = []
totalDates = []
totalPlayerLeavingInjury = []
totalPlayerOnInjury = []
season = []
totalLastName = []
totalFirstName = []
daysCalculated = []

lastOne = ""
firstTwo = ""
lastFive = ""
cols = []
header = ""
player = []
years = []
page = 0
header = []
rows = []
totalFile = []
wasRelinquished = False
wasRelinquishedDate = ""
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
def FilterProSportsTransactions(line,filterDate=[],filterTeam=[],filterPlayerLeavingInjury=[],filterPlayerOnInjury=[],filterInjury=[]):
    filterDate.append(line.split(',')[0])
    filterTeam.append(line.split(',')[1])
    filterPlayerLeavingInjury.append(line.split(',')[2])
    filterPlayerOnInjury.append(line.split(',')[3])
    if len(line.split(',')[4]) != 10:
        filterInjury.append(line.split(',')[4])
    if (len(playerOnInjury[number]) == 3):
        playerLastName.append(playerLeavingInjury[number].split(" ")[3])
        playerFirstName.append(playerLeavingInjury[number].split(" ")[2])
    elif (len(playerLeavingInjury[number]) == 3):
        playerLastName.append(playerOnInjury[number].split(" ")[3])
        playerFirstName.append(playerOnInjury[number].split(" ")[2])
for line in file1:
    #/////////////////////////////////
    # Title: Split a String and get First or Last element in Python
    # Name: Borislav Hadzhiev
    # Site Owner: Bobbyhadz
    # Date: Feb. 19, 2023
    # Code-Version: N/A
    # Availability: https://bobbyhadz.com/blog/python-split-string-and-get-last-element
    # Modified: Yes
    totalFile.append(line)
    FilterProSportsTransactions(line,date,team,playerLeavingInjury,playerOnInjury,injury)
    number += 1
#/////////////////////////////////
# Title: How to Remove Quotes from Strings in Python
# Name: Dimitrije Stamenic
# Site Owner: StackAbuse
# Date: June 1, 2023
# Code-Version: N/A
# Availability: https://stackabuse.com/how-to-remove-quotes-from-string-in-python/
# Modified: Yes
def cleaning_results(itemToClean):
    itemToClean = itemToClean.replace("'","")
    itemToClean = itemToClean.replace('"','')
    itemToClean = itemToClean.replace('[','')
    itemToClean = itemToClean.replace("]","")
    return itemToClean
def calculate_days():
    for i in range(len(totalFirstName)):
        if len(totalPlayerLeavingInjury[i]) > 1:
            if wasRelinquished == True:
                newDate = datetime.strptime(totalDates[i],'%Y-%m-%d') - datetime.strptime(wasRelinquishedDate,'%Y-%m-%d')
                daysCalculated.append(newDate.days)
            else:
                daysCalculated.append(0)    
            wasRelinquished = False
        elif len(totalPlayerOnInjury[i]) > 1:
            wasRelinquished = True
            wasRelinquishedDate = totalDates[i]
            daysCalculated.append(0)
        else:
            daysCalculated.append(0)
            
def calculate_season_dates():
    calculate_season_numerator = 0
    for i in totalDates:
        newDate = datetime.strptime(totalDates[calculate_season_numerator],'%Y-%m-%d')
        if newDate <= datetime(2024,6,13) and newDate >= datetime(2022,9,10):
            season.append("2023-24")
        elif newDate <= datetime(2023,6,13) and newDate >= datetime(2022,9,7):
            season.append("2022-23")
        elif newDate <= datetime(2022,6,26) and newDate >= datetime(2021,9,12):
            season.append("2021-22")
        elif newDate <= datetime(2021,7,7) and newDate >= datetime(2021,1,13):
            season.append("2020-21")
        elif newDate <= datetime(2020,8,28) and newDate >= datetime(2019,9,2):
            season.append("2019-20")
        elif newDate <= datetime(2019,6,12) and newDate >= datetime(2018,9,3):
            season.append("2018-19")
        elif newDate <= datetime(2018,6,7) and newDate >= datetime(2017,9,4):
            season.append("2017-18")
        elif newDate <= datetime(2017,6,11) and newDate >= datetime(2016,9,12):
            season.append("2016-17")
        elif newDate <= datetime(2016,6,12) and newDate >= datetime(2015,9,7):
            season.append("2015-16")
        elif newDate <= datetime(2015,6,15) and newDate >= datetime(2014,9,8):
            season.append("2014-15")
        elif newDate <= datetime(2014,6,13) and newDate >= datetime(2013,9,1):
            season.append("2013-14")
        elif newDate <= datetime(2013,6,24) and newDate >= datetime(2013,1,19):
            season.append("2012-13")
        elif newDate <= datetime(2012,6,11) and newDate >= datetime(2011,9,6):
            season.append("2011-12")
        elif newDate <= datetime(2011,6,15) and newDate >= datetime(2010,9,7):
            season.append("2010-11")
        elif newDate <= datetime(2010,6,9) and newDate >= datetime(2009,9,1):
            season.append("2009-10")
        elif newDate <= datetime(2009,6,12) and newDate >= datetime(2008,9,4):
            season.append("2008-09")
        elif newDate <= datetime(2008,6,4) and newDate >= datetime(2007,8,29):
            season.append("2007-08")
        elif newDate <= datetime(2007,6,6) and newDate >= datetime(2006,9,4):
            season.append("2006-07")
        elif newDate <= datetime(2006,6,19) and newDate >= datetime(2005,9,5):
            season.append("2005-06")
        elif newDate <= datetime(2004,6,7) and newDate >= datetime(2003,9,8):
            season.append("2003-04")
        elif newDate <= datetime(2003,6,9) and newDate >= datetime(2002,9,9):
            season.append("2002-03")
        else:
            season.append("")
        calculate_season_numerator += 1
iterator = 0
for cleaningList in playerLastName:
    playerLastName[iterator] = cleaning_results(playerLastName[iterator])
    playerFirstName[iterator] = cleaning_results(playerFirstName[iterator])
    date[iterator] = cleaning_results(date[iterator])
    injury[iterator] = cleaning_results(injury[iterator])
    team[iterator] = cleaning_results(team[iterator])
    iterator += 1
newIterator = 0
name = 0
number = -1
for i in totalFile:
    injuryIter = 0
    injuryDataset = []
    injuryURL =  "https://www.prosportstransactions.com/hockey/Search/SearchResults.php?Player=" + playerFirstName[name] + "+" + playerLastName[name] + "&Team=&BeginDate=&EndDate=&ILChkBx=yes&submit=Search&start=0"
    response =requests.get(injuryURL.format())
    soup=BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    for i, row in enumerate(table.find_all('tr')):
        if i != 0:
            injuryDataset.append([el.text.strip() for el in row.find_all('td')])
    for i in injuryDataset:
        injuryDataset[injuryIter] = cleaning_results(str(injuryDataset[injuryIter]))
        FilterProSportsTransactions(str(injuryDataset[injuryIter]),totalDates,totalTeam,totalPlayerLeavingInjury,totalPlayerOnInjury,totalInjury)
        #print(str(playerFirstName[name]) + " " + str(playerLastName[name]) + " " + str(totalDates[name]))
        injuryIter += 1
    number += 1
    name += 1
temp = 0
name = 0
calculate_season_dates()
#print(totalPlayerOnInjury)
for cleaningList in totalPlayerOnInjury:
    if (len(totalPlayerOnInjury[newIterator]) > 4):
        totalLastName.append(totalPlayerOnInjury[newIterator].split(" ")[3])
        totalFirstName.append(totalPlayerOnInjury[newIterator].split(" ")[2])
    elif (len(totalPlayerLeavingInjury[newIterator]) > 4):
        totalLastName.append(totalPlayerLeavingInjury[newIterator].split(" ")[3])
        totalFirstName.append(totalPlayerLeavingInjury[newIterator].split(" ")[2])
    totalLastName[newIterator] = cleaning_results(totalLastName[newIterator])
    totalFirstName[newIterator] = cleaning_results(totalFirstName[newIterator])
    newIterator += 1
calculate_days()
def injury_calc(first_name,last_name,date):
    injuryData = []
    new_string = "0"
    for i in range(len(totalFirstName)):
        date = date.replace("-","")
        season[i] = season[i].replace("-","")
        #print(str(date.strip()) + str(season[i].strip()))
        if totalFirstName[i] == first_name and totalLastName[i] == last_name and season[i].strip() == date.strip() and daysCalculated[i] != 0:
            injuryData.remove(0)
            injuryData.append(daysCalculated[i])
    for element in injuryData:
        if new_string == "0":
            new_string = ""
        new_string += str(element) 
        new_string += ","
    return str(new_string)
    #return 0
for data in totalFile:
    lastOne = playerLastName[name][0].lower()
    firstTwo = playerFirstName[name][0].lower() + playerFirstName[name][1]
    lastFive = playerLastName[name][0 : 5].lower()
    url = "https://www.hockey-reference.com/players/" + lastOne + "/" + lastFive + firstTwo + "01.html"
    print(url)
    time.sleep(5)
    response =requests.get(url.format())
    soup=BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', id="stats_basic_plus_nhl")
    pageNumb = 10
    while (table is None and pageNumb > 0):
        url = "https://www.hockey-reference.com/players/" + lastOne + "/" + lastFive + firstTwo + "0" + str(pageNumb) + ".html"
        response =requests.get(url.format())
        soup=BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', id="stats_basic_plus_nhl")
        pageNumb -= 1
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
            if e[1] != "":
                cols.append([playerFirstName[name], playerLastName[name], date[name], team[name], injury[name], e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13],e[14],e[15],
                e[16],e[17],e[18],e[19],e[20],e[21],e[22],e[23],e[24],e[25],e[26],e[27],e[28],e[29],injury_calc(playerFirstName[name],playerLastName[name], e[0])])
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
                  "Time on Minutes","Average Time on Ice","Faceoff Wins","Faceoff Losses","Faceoff Percentage","Blocks","Hits","Takeaways","Giveaways","Awards","Injury Time"])
df.to_csv("playerData.csv")
file1.close()
print("finished")