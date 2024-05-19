import requests
from bs4 import BeautifulSoup

base_site = 'https://www.vgchartz.com/games/games.php?name=&keyword=&console=&region=All&developer=&publisher=&goty_year=&genre=Misc&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=1000&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&shownasales=0&shownasales=1&showdeveloper=0&showdeveloper=1&showcriticscore=0&showpalsales=0&showpalsales=1&showreleasedate=0&showreleasedate=1&showuserscore=0&showjapansales=0&showjapansales=1&showlastupdate=0&showothersales=0&showothersales=1&showshipped=0&showshipped=1'

response = requests.get(base_site)
response

html = response.content

soup = BeautifulSoup(html, 'lxml')

with open('vgchartz_page_HTML_parser.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

#First let's extract all of the tables from the site
tables = soup.find_all("table")
tables

# We find that the 7th table is table that contains all of video game sales info we want
table = soup.find_all("table")[6]
table

#Now let's extract all of the rows from our table
table.find_all('tr')

#We find that rows 1-3 are NOT needed as they are headers, etc
table.find_all('tr')[3].contents

#We make a list of games starting from row 4 onward
game_rows = table.find_all('tr')[3:]
game_rows

#We confirm the list contains all of the games in the table
len(game_rows)

#For each row, there are 2 'a' elements and we selectively choose to pull the 2nd one as it contains the title of the video game
titles = [game_row.find_all('a')[1].string for game_row in game_rows]
titles

titles[0]

len(titles)

titles = [title.strip('    ') for title in titles]
titles

#Contents[7] = Console, Contents[9] = Publisher, Contents[11] = Developer
game_rows[0].contents

consoles = [game_row.contents[7].find('img').attrs['alt'] for game_row in game_rows]
consoles


publishers = [game_row.contents[9].text for game_row in game_rows]
publishers = [publisher.strip('  ') for publisher in publishers]
publishers

developers = [game_row.contents[11].text for game_row in game_rows]
developers = [developer.strip('  ') for developer in developers]
developers

#Contents[13] = Total Units Shipped, Contents[15] = Total Sales, Contents[17] = NA Sales, Contents[19] = PAL Sales,  
#Contents[21] = Japan Sales, Contents[23] = Other Sales, Contents[25] = Release Date
game_rows[0].contents


units_sold = [game_row.contents[13].text for game_row in game_rows]
units_sold

total_sales = [game_row.contents[15].text for game_row in game_rows]
total_sales


na_sales = [game_row.contents[17].text for game_row in game_rows]
na_sales

pal_sales = [game_row.contents[19].text for game_row in game_rows]
pal_sales

jp_sales = [game_row.contents[21].text for game_row in game_rows]
jp_sales

other_sales = [game_row.contents[23].text for game_row in game_rows]
other_sales

release_dates = [game_row.contents[25].text for game_row in game_rows]
release_dates = [release_date.strip('  ') for release_date in release_dates]
release_dates



import requests
from bs4 import BeautifulSoup


genre_page = ['Adventure', 'Action', 'Action-Adventure', 'Board+Game', 'Education', 'Fighting', 'Misc', 'MMO', 'Music', 'Party',
          'Platform', 'Puzzle', 'Racing', 'Role-Playing', 'Sandbox', 'Shooter', 'Simulation', 'Sports', 'Strategy', 'Visual+Novel']


titles = []
consoles = []
genres = []
publishers = []
developers = []
units_sold = []
total_sales = []
na_sales = []
pal_sales = []
jp_sales = []
other_sales =[]
release_dates = []

base_site_1 = 'https://www.vgchartz.com/games/games.php?name=&keyword=&console=&region=All&developer=&publisher=&goty_year=&genre='

base_site_2 ='&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=10000&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showpublisher=1&showvgchartzscore=0&shownasales=0&shownasales=1&showdeveloper=0&showdeveloper=1&showcriticscore=0&showpalsales=0&showpalsales=1&showreleasedate=0&showreleasedate=1&showuserscore=0&showjapansales=0&showjapansales=1&showlastupdate=0&showothersales=0&showothersales=1&showshipped=0&showshipped=1'

len(genre_page)

for page in range(0, len(genre_page)):
    print('Scraping Page ' + str(page+1) + '...')
    
    base_site = base_site_1 + genre_page[page] + base_site_2
    html = requests.get(base_site).content
    soup = BeautifulSoup(html, 'lxml')
    
    table = soup.find_all("table")[6]
    game_rows = table.find_all('tr')[3:]
    
    #Game Titles
    titles_temp = [game_row.find_all('a')[1].string for game_row in game_rows]
    titles_temp = [title.strip('    ') for title in titles_temp]
    titles.extend(titles_temp)
    
    #Genres
    #Simply applies the genre from the genre page we are pulling data from and appending to list
    for i in range(0, len(titles_temp)):
        genres.append(genre_page[page])
    
    #Consoles
    consoles_temp = [game_row.contents[7].find('img').attrs['alt'] for game_row in game_rows]
    consoles.extend(consoles_temp)
    
    #Publishers
    publishers_temp = [game_row.contents[9].text for game_row in game_rows]
    publishers_temp = [publisher.strip('  ') for publisher in publishers_temp]
    publishers.extend(publishers_temp)
    
    #Developers
    developers_temp = [game_row.contents[11].text for game_row in game_rows]
    developers_temp = [developer.strip('  ') for developer in developers_temp]
    developers.extend(developers_temp)
    
    #Units Sold
    units_sold_temp = [game_row.contents[13].text for game_row in game_rows]
    units_sold.extend(units_sold_temp)
    
    #Total Sales
    total_sales_temp = [game_row.contents[15].text for game_row in game_rows]
    total_sales.extend(total_sales_temp)
    
    #NA Sales
    na_sales_temp = [game_row.contents[17].text for game_row in game_rows]
    na_sales.extend(na_sales_temp)
    
    #PAL Sales
    pal_sales_temp = [game_row.contents[19].text for game_row in game_rows]
    pal_sales.extend(pal_sales_temp)
    
    #JP Sales
    jp_sales_temp = [game_row.contents[21].text for game_row in game_rows]
    jp_sales.extend(jp_sales_temp)
    
    #Other Sales
    other_sales_temp = [game_row.contents[23].text for game_row in game_rows]
    other_sales.extend(other_sales_temp)
    
    #Release Dates
    release_dates_temp = [game_row.contents[25].text for game_row in game_rows]
    release_dates_temp = [release_date.strip('  ') for release_date in release_dates_temp]
    release_dates.extend(release_dates_temp)


game_info = pd.DataFrame()

game_info["Video Game Title"] = titles
game_info['Genre'] = genres
game_info['Console'] = consoles
game_info['Publishers(s)'] = publishers
game_info['Developer(s)'] = developers
game_info['Units Sold'] = units_sold
game_info['Total Sales'] = total_sales
game_info['NA Sales'] = na_sales
game_info['PAL Sales'] = pal_sales
game_info['JP Sales'] = jp_sales
game_info['Other Sales'] = other_sales
game_info['Release Date'] = release_dates

game_info


game_info.to_csv("../Data/game_info.csv", index = False, header = True)
game_info.to_excel("../Data/game_info.xlsx", index = False, header = True)