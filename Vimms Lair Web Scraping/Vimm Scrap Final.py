import requests
from bs4 import BeautifulSoup  
import pandas as pd 

start = 1001
stop = 9775
j = start
records = []
k=0

while j <= stop:

    #skip 20

    ID = str(j)
    url= "https://vimm.net/vault/" + ID

    req= requests.get(url)
    #print(req.text[0:500])

    soup = BeautifulSoup(req.text, 'html.parser')

    results = soup.find_all('div', attrs={'id':'innerMain'})
    tr = soup.find_all('tr')

    #Pull Player numbers
    try:
        tr6=tr[6].contents[5].text
        players = tr6[2]
    except:
        players = 0


    #Pull Year of publish
    try:
        tr7 = tr[7].contents[5].text
        if tr7 == '?':
            year = tr7
        else:
            year=int(tr[7].contents[5].text)
    except:
        year = 0

    #Pull File size and convert to MB
    try:
        tr8 = tr[8].contents[5].text
        size_num = float(tr8[:-3])
        size_unit = str(tr8[-2:])
        if size_unit == 'KB':
            size_num =size_num /1000
            size_unit = "MB"
        elif size_unit =='GB':
            size_num = size_num*1000
            size_unit = "MB"
    except:
        size_num = 0
        size_unit = '?'

    #Create ID number related to URL
    GameID = j

    #Parse results for console and title
    try:
        for result in results:
            console = result.find('span', attrs={'class':'sectionTitle'}).text  
            title = result.find('span', attrs={'style':'text-decoration:underline'}).text
    except:
        console = '?'
        title = '?'

    #Compile results into a data record

    records.append((GameID, console, title, size_num,size_unit, players,year))
    print(records[k])
    
    k=k+1
    j=j+1


 
df = pd.DataFrame(records, columns=['Game ID', 'Console', 'Title', 'Size', 'Unit','Players', 'Publish Year'])  
#df['date'] = pd.to_datetime(df['date'])  
df.to_csv('C:\\Users\\agerman\\Desktop\\3D Printing\\Web Scraping Results\\Vimms Lair Game List ' + str(start) + ' - ' + str(stop) + '.csv', index=False, encoding='utf-8')
print("Export Complete")
#error handling necessary for game 9725 game not found

