from bs4 import BeautifulSoup
import requests
res = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(res.text, 'lxml')
stat_table = soup.select('#main_table_countries_today')
#print(stat_table )

with open('worldometer1.txt','w') as r:
    for stat in stat_table.find_all('tbody'):
        rows = stat.find_all ('tr ')
        td = tr.find_all('td')
        row = [i.text for i in td]
        #print(row)

        row_string = "  ".join(row)
        print(row_string)
        r.write(row_string )
        r.write('\n')

#f.close