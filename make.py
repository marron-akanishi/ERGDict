import io
import jaconv
from bs4 import BeautifulSoup

html = open('source.html','rt',encoding='UTF-8')
out = open('ergtitle.txt','wt',encoding='UTF-8')
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')

for i,data in enumerate(table.find_all('tr')):
    if i == 0:
        continue
    text = ""
    name = data.find_all('td')
    text += jaconv.kata2hira(name[0].string) + "\t"
    text += name[1].string + "\t"
    text += "固有名詞\n"
    out.write(text)

out.close()