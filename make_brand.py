import io
import requests
import jaconv
from bs4 import BeautifulSoup

def make(circle, lost):
    if circle == False and lost == False:
        basetext = "SELECT brandfurigana,brandname FROM brandlist WHERE "
    else:
        basetext = "SELECT brandfurigana,brandname FROM brandlist "
    if circle == False:
        basetext += "kind = 'CORPORATION' AND "
    if lost == False:
        basetext += "lost = 'FALSE' "
    basetext += "ORDER BY brandfurigana"
    url = "http://erogamescape.dyndns.org/~ap2/ero/toukei_kaiseki/sql_for_erogamer_form.php"
    s = requests.session()
    payload = {'sql': basetext}
    r =  s.post(url, data=payload)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    text = ""
    for i,row in enumerate(table.find_all('tr')):
        if i == 0:
            continue
        data = row.find_all('td')
        text += "{furigana}\t{name}\t固有名詞\n".format(furigana=jaconv.kata2hira(data[0].string), name=data[1].string)
    return text

if __name__ == "__main__":
    out = open('ergbrand.txt','wt',encoding='UTF-8')
    out.write(make(False,False))
    out.close()