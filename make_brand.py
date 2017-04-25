import io
import requests
import jaconv
from bs4 import BeautifulSoup

url = "http://erogamescape.dyndns.org/~ap2/ero/toukei_kaiseki/sql_for_erogamer_form.php"
s = requests.session()
payload = {'sql': "SELECT brandfurigana,brandname FROM brandlist WHERE kind = 'CORPORATION' \
            AND lost = 'FALSE' ORDER BY brandfurigana"}
r =  s.post(url, data=payload)
html = r.text

out = open('ergbrand.txt','wt',encoding='UTF-8')
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')

for i,row in enumerate(table.find_all('tr')):
    if i == 0:
        continue
    text = ""
    data = row.find_all('td')
    text = "{furigana}\t{name}\t固有名詞\n".format(furigana=jaconv.kata2hira(data[0].string), name=data[1].string)
    out.write(text)

out.close()