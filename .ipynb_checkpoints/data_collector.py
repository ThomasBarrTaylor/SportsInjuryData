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
START_DATE="2017-11-04"
END_DATE="2017-11-08"
page=0
rows=[]
totalFile = []
HTML_PARSER = "html.parser"
#/////////////////////////////////
# Title: How to scrape tables with BeautifulSoup?
# Name: Dimitrije Stamenic
# Site Owner: ScrapFly
# Date: OCt. 24, 2022
# Code-Version: N/A
# Availability: https://scrapfly.io/blog/how-to-scrape-tables-with-beautifulsoup/
# Modified: Yes
url = "https://www.prosportstransactions.com/hockey/Search/SearchResults.php?Player=&Team=&BeginDate={}&EndDate={}&ILChkBx=yes&submit=Search&start={}"

def cleaning_results(item_to_clean):
    item_to_clean = item_to_clean.replace("'","")
    item_to_clean = item_to_clean.replace('"','')
    item_to_clean = item_to_clean.replace('[','')
    item_to_clean = item_to_clean.replace("]","")
    return item_to_clean

def filter_pro_sports_transactions(line,func_player):
    
    func_dates = line.split(',')[0]
    func_teams = line.split(',')[1]
    func_leaving_injury = line.split(',')[2]
    func_on_injury = line.split(',')[3]
    func_injury = line.split(',')[4]
    new_player = []
    if len(func_on_injury) == 3 and len(func_leaving_injury.split(" ")) > 3:
            if len(line.split(',')[4]) != 10:
                new_player = [func_leaving_injury.split(" ")[2],func_leaving_injury.split(" ")[3],func_dates,func_teams,func_injury,"True"]
    elif len(func_leaving_injury) == 3 and len(func_on_injury.split(" ")) > 3:
            if len(line.split(',')[4]) != 10:
                new_player = [func_on_injury.split(" ")[2],func_on_injury.split(" ")[3],func_dates,func_teams,func_injury,"False"]
    if new_player:
        func_player.append(new_player)

def calc_ending_dates(new_date):
    end_date =""
    new_date = datetime.strptime(new_date,'%Y-%m-%d')
    if new_date >= datetime(2023,9,10):
        end_date = datetime(2024,6,13)
    elif new_date >= datetime(2022,9,7):
        end_date = datetime(2023,6,13)
    elif new_date >= datetime(2021,9,12):
        end_date = datetime(2022,6,26)
    elif new_date >= datetime(2021,1,13):
        end_date = datetime(2021,7,7)
    elif new_date >= datetime(2019,9,2):
        end_date = datetime(2020,8,28)
    elif new_date >= datetime(2018,9,3):
        end_date = datetime(2019,6,12)
    elif new_date >= datetime(2017,9,4):
        end_date = datetime(2018,6,7)
    elif new_date >= datetime(2016,9,12):
        end_date = datetime(2017,6,11)
    elif new_date >= datetime(2015,9,7):
        end_date = datetime(2016,6,12)
    elif new_date >= datetime(2014,9,8):
        end_date = datetime(2015,6,15)
    elif new_date >= datetime(2013,9,1):
        end_date = datetime(2014,6,13)
    elif new_date >= datetime(2013,1,19):
        end_date = datetime(2013,6,24)
    elif new_date >= datetime(2011,9,6):
        end_date = datetime(2012,6,11)
    elif new_date >= datetime(2010,9,7):
        end_date = datetime(2011,6,15)
    elif new_date >= datetime(2009,9,1):
        end_date = datetime(2010,6,9)
    elif new_date >= datetime(2008,9,4):
        end_date = datetime(2009,6,12)
    if end_date:
        end_date = end_date - new_date
        return end_date.days
    else:
        return 0
    
def calculate_season_dates(new_dates):
    season = ""
    for i in new_dates:
        if len(new_dates) > 10:
            new_date = datetime.strptime(i,'%Y-%m-%d')
        else:
            new_date = datetime.strptime(new_dates,'%Y-%m-%d')

        if new_date >= datetime(2023,9,10):
            season ="2023-24" 
        elif datetime(2023,6,13) >= new_date >= datetime(2022,9,7):
            season ="2022-23"
        elif datetime(2022,6,26) >= new_date >= datetime(2021,9,12):
            season = "2021-22"
        elif datetime(2021,7,7) >= new_date >= datetime(2021,1,13):
            season = "2020-21"
        elif datetime(2020,8,28) >= new_date >= datetime(2019,9,2):
            season = "2019-20"
        elif datetime(2019,6,12) >= new_date >= datetime(2018,9,3):
            season = "2018-19"
        elif datetime(2018,6,7) >= new_date >= datetime(2017,9,4):
            season = "2017-18"
        elif datetime(2017,6,11) >= new_date >= datetime(2016,9,12):
            season = "2016-17"
        elif datetime(2016,6,12) >= new_date >= datetime(2015,9,7):
            season = "2015-16"
        elif datetime(2015,6,15) >= new_date >= datetime(2014,9,8):
            season = "2014-15"
        elif datetime(2014,6,13) >= new_date >= datetime(2013,9,1):
            season = "2013-14"
        elif datetime(2013,6,24) >= new_date >= datetime(2013,1,19):
            season ="2012-13"
        elif datetime(2012,6,11) >= new_date >= datetime(2011,9,6):
            season = "2011-12"
        elif datetime(2011,6,15) >= new_date >= datetime(2010,9,7):
            season = "2010-11"
        elif datetime(2010,6,9) >= new_date >= datetime(2009,9,1):
            season ="2009-10"
        elif datetime(2009,6,12) >= new_date >= datetime(2008,9,4):
            season ="2008-09"
        elif datetime(2008,6,4) >= new_date >= datetime(2007,8,29):
            season ="2007-08"
        elif datetime(2007,6,6) >= new_date >= datetime(2006,9,4):
            season = "2006-07"
        elif datetime(2006,6,19) >= new_date >= datetime(2005,9,5):
            season ="2005-06"
        elif datetime(2004,6,7) >= new_date >= datetime(2003,9,8):
            season = "2003-04"
        elif datetime(2003,6,9) >= new_date >= datetime(2002,9,9):
            season = "2002-03"
        else:
            season = ""
    return season

def calculate_days(total_player_list):
    was_relinquished = False
    was_out_for_season = False
    was_out_for_season_date = ""
    days = 0
    for i in range(len(total_player_list)):
        if total_player_list[i][5] == "True":
            if was_relinquished == True and calculate_season_dates(was_relinquished_date) == calculate_season_dates(total_player_list[i][2]):
                new_date = datetime.strptime(total_player_list[i][2],'%Y-%m-%d') - datetime.strptime(was_relinquished_date,'%Y-%m-%d')

                days = new_date.days
            else:
                days = 0
            was_relinquished = False
        elif total_player_list[i][5] == "False":
            if "(out for season)" in total_player_list[i][4]:
                if was_out_for_season == True and was_out_for_season_date == calculate_season_dates(total_player_list[i][2]):
                    days = 0
                else:  
                    days = calc_ending_dates(total_player_list[i][2])
                was_out_for_season = True
                was_out_for_season_date = calculate_season_dates(total_player_list[i][2])
                was_relinquished = False
            elif "undisclosed" in total_player_list[i][4] or "COVID-19" in total_player_list[i][4] or "illness" in total_player_list[i][4]:
                days = 0
                was_relinquished = False
            else:
                was_relinquished = True
                was_relinquished_date = total_player_list[i][2]
                days = 0
        else:
            days = 0
        total_player_list[i].append(days)

def injury_calc(first_name,last_name,date,total_player_list):
    injury_data = []
    injury_desc = []
    cumalitive_injury = 0
    for i in range(len(total_player_list)):
        if total_player_list[i][0] == first_name and total_player_list[i][1] == last_name and date == calculate_season_dates(total_player_list[i][2]) and int(total_player_list[i][6]) > 0:
            if "out for season" in total_player_list[i][4]:
                injury_desc.append(total_player_list[i][4])
            else:
                injury_desc.append(total_player_list[i-1][4])
            if injury_data[0] == 0:
                injury_data.remove(0)
            injury_data.append(total_player_list[i][6])
            cumalitive_injury += total_player_list[i][6]
        elif not injury_data:
            injury_data.append(0)
    return str(injury_data),str(cumalitive_injury),str(injury_desc)

def to_csv(array,file):
    df = pd.DataFrame(array,columns=["Player First Name","Player Last Name", "Position", "Season","Age","Team","League",
                  "Games Played","Goals","Assists","Points","+/-","Penalties in Minutes","Even Strength Goals","Power Play Goals","Short Handed Goals",
                  "Game-Winning Goals","Even Strength Assists","Power Play Assists","Short-Handed Assists","Shots On Goals","Shooting Percentage","Total Shoot Assists",
                  "Time on Minutes","Average Time on Ice","Faceoff Wins","Faceoff Losses","Faceoff Percentage","Blocks","Hits","Takeaways","Giveaways","Awards","Injury Time","Total Time Out This Year","Injury Description"])
    df.to_csv(file, encoding = 'utf-8-sig' )

def convert_array(no_dup_list,season):
    stats_array = []
    for e in no_dup_list:
        if e:
            stats_array.append([e[0].split(' ')[0],e[0].split(' ')[1],e[3],season,e[1],e[2],
                                "NHL",e[4],e[5],e[6],e[7],e[8],e[9],e[11],e[12],e[13],e[14],
                                e[15],e[16],e[17],e[18],e[19],"",e[20],e[21],e[24],e[25],
                                e[26],e[22],e[23],"","","","","",""])
    return stats_array

def check_duplicates(current_array):
    previous_season = ""
    previous_first_name = ""
    previous_last_name = ""
    previously_traded = False
    new_array =[]
    append_bool = False

    for e in current_array:

        if previously_traded == True:
            if e[3] != previous_season or e[0] != previous_first_name or e[1] != previous_last_name:
                append_bool =True
            else:
                append_bool=False
        else:
            append_bool=True
            previously_traded = False
        if e[5] == "TOT":
            previously_traded = True
        
        if append_bool:
            new_array.append(e)
        previous_season = e[3]
        previous_first_name = e[0]
        previous_last_name = e[1]
    return new_array

def create_control_group(yearly_data,injury_data):
    function_array = []
    for i in yearly_data:
        for j in injury_data:
            if i[0] == j[0] and i[1] == j[1]:
                break
        else:
            function_array.append(i)

    return function_array

initial_player_list=[]
response =requests.get(url.format(START_DATE,END_DATE,page))
soup=BeautifulSoup(response.content, HTML_PARSER)
table = soup.find('table')
while (len(table.find_all('tr')) > 1):
    page +=25
    print("page: " + str(page))
    for i, row in enumerate(table.find_all('tr')):
        if i > 0:
            rows.append([el.text.strip() for el in row.find_all('td')])
    response =requests.get(url.format(START_DATE,END_DATE,page))
    soup=BeautifulSoup(response.content, HTML_PARSER)
    table = soup.find('table')
rows_without_duplicates = []
a = set()
for i in range(len(rows)):
    if rows[i][2]:
        inner_tuple = tuple(rows[i][2])
    elif rows[i][3]:
        inner_tuple = tuple(rows[i][3])
    if inner_tuple not in a:
        rows_without_duplicates.append(rows[i])
        a.add(inner_tuple)
file1.writelines("% s\n" % data for data in rows_without_duplicates)
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
    totalFile.append(line)
    filter_pro_sports_transactions(line,initial_player_list)
file1.close()  
#/////////////////////////////////
# Title: How to Remove Quotes from Strings in Python
# Name: Dimitrije Stamenic
# Site Owner: StackAbuse
# Date: June 1, 2023
# Code-Version: N/A
# Availability: https://stackabuse.com/how-to-remove-quotes-from-string-in-python/
# Modified: Yes
for iter in range(len(initial_player_list)):
    for numb in range(len(initial_player_list[iter])):
        initial_player_list[iter][numb] = cleaning_results(initial_player_list[iter][numb])
newIterator = 0
name = 0

rows_above_zero = []
year_data_above_zero = []
total_player = []
total_player_list = []
for i in initial_player_list:
    player_pages = 0
    injury_iter = 0
    injury_dataset = []
    injuryURL =  "https://www.prosportstransactions.com/hockey/Search/SearchResults.php?Player=" + i[0] + "+" + i[1] + "&Team=&BeginDate=&EndDate=&ILChkBx=yes&submit=Search&start={}"
    response =requests.get(injuryURL.format(player_pages))
    soup=BeautifulSoup(response.content, HTML_PARSER)
    table = soup.find('table')
    if table:
        for i, row in enumerate(table.find_all('tr')):
            if i != 0:
                injury_dataset.append([el.text.strip() for el in row.find_all('td')])
        if len(table.find_all('tr')) == 26:
            player_pages += 25
            response =requests.get(injuryURL.format(player_pages))
            soup=BeautifulSoup(response.content, HTML_PARSER)
            table = soup.find('table')
            for i, row in enumerate(table.find_all('tr')):
                if i != 0:
                    injury_dataset.append([el.text.strip() for el in row.find_all('td')])
           
    for i in range(len(injury_dataset)):
        filter_pro_sports_transactions(str(injury_dataset[i]),total_player_list)
        
    for i in range(len(total_player_list)):
        for e in range(len(total_player_list[i])):
            total_player_list[i][e] = cleaning_results(total_player_list[i][e])

calculate_days(total_player_list)

cols = []
new_rows = []
year_data = []
for data in initial_player_list:
    last_one = data[1][0].lower()
    first_two = data[0][0].lower() + data[0][1].lower()
    last_five = data[1][0:5].lower()
    pageNumb = 1
    table = None
    #while (table is None and pageNumb > 0):
    time.sleep(3.5)
    url = "https://www.hockey-reference.com/players/" + last_one + "/" + last_five + first_two + "0" + str(pageNumb) + ".html"
    print(url)
    response =requests.get(url.format())
    soup=BeautifulSoup(response.content, 'html.parser')
    strong = soup.find('strong',string="Position")
    if strong:
        new_strong = str(strong.next_sibling.text.split(" ")[1])
        new_strong = new_strong[0]
    if new_strong == 'R':
        new_strong = 'RW'
    elif new_strong == 'L':
        new_strong = 'LW'
    new_strong = [new_strong]
    #rows.append(strong.next_sibling)
    table = soup.find('table', id="stats_basic_plus_nhl")
    pageNumb -= 1
    if table is not None:
        for i, row in enumerate(table.find_all('tr')):
            if i == 0 or i == 1:
                header = [el.text.strip() for el in row.find_all('th')]
            else:
                years = [el.text.strip() for el in row.find_all('th')]
                player = [el.text.strip() for el in row.find_all('td')]
                final_rows.append(new_strong + years + player)
    l = ""
    repeat_player = ""
    if (len(final_rows)>0) and len(final_rows[0])==31:
        for e in final_rows:
            if e[2] != "":
                t1,t2,t3 = injury_calc(data[0],data[1], e[1],total_player_list)
                cols.append([data[0], data[1], e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13],e[14],e[15],
                e[16],e[17],e[18],e[19],e[20],e[21],e[22],e[23],e[24],e[25],e[26],e[27],e[28],e[29],e[30],str(t1)[1:-1],t2,str(t3)[1:-1]])
                #if int(t2) > 0 and e[1] == "2021-22":
                    #year_data.append(player_first_name[name], player_last_name[name],e)
                #if int(t2) <= 0:
                    #del new_rows[-1]
    final_rows = []
#l,repeat_player,t2,new_rows = check_duplicates(l,repeat_player,player_first_name,player_last_name,cols,season)
#/////////////////////////////////////////
# Title: pandas.DataFrame.to_csv
# Name: N/A
# Site Owner: Pandas
# Date: N/A
# Code-Version: 2.1.3
# Availability: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
# Modified: Yes

hockey_year = "2021-22"
year_skaters = "20" + hockey_year[5:7]
yearlyURL =  "https://www.hockey-reference.com/leagues/NHL_" + year_skaters + "_skaters.html"
yearly_dataset = []
stats_array = []
response =requests.get(yearlyURL.format())
soup=BeautifulSoup(response.content, HTML_PARSER)
table = soup.find('table', id="stats")
for i, row in enumerate(table.find_all('tr')):
    if i > 1:
        yearly_dataset.append([el.text.strip() for el in row.find_all('td')])
stats_array = convert_array(yearly_dataset,hockey_year)

new_rows_above_zero = []
new_player_data = []
for e in cols:
    if int(e[34]) > 0:
        rows_above_zero.append(e)
        if e[3] == hockey_year:
            year_data_above_zero.append(e)
        else:
            new_rows_above_zero.append(e)
    if e[3] != hockey_year:
        new_player_data.append(e)

stats_array = check_duplicates(stats_array)
control_group = []
control_group = create_control_group(stats_array,year_data_above_zero)

all_players = []
no_dup_players = []
new_player_data =check_duplicates(new_player_data)

new_rows_above_zero = check_duplicates(new_rows_above_zero)
year_data_above_zero = check_duplicates(year_data_above_zero)

to_csv(new_player_data,"player_data.csv")
to_csv(new_rows_above_zero,"player_injuries.csv")
to_csv(control_group,"yearly_data.csv")
to_csv(year_data_above_zero,"yearly_data_above_zero.csv")
print("finished")