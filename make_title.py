import io
import jaconv
import requests
from bs4 import BeautifulSoup

def make(start, unknown, okazu):
    basetext = "SELECT g.furigana,g.gamename,b.brandname,g.sellday FROM gamelist g INNER JOIN brandlist b ON b.id = g.brandname WHERE "
    basetext += "sellday >= '{}' ".format(start)
    if unknown == False:
        basetext += "AND sellday <> '2030-01-01' "
    if okazu == False:
        basetext += "AND okazu <> 't' "
    basetext += "ORDER BY g.furigana"
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
        text += "{furigana}\t{title}\t固有名詞\tブランド名：{brand}｜発売日：{sellday}\n"\
                .format(furigana=jaconv.kata2hira(data[0].string), title=data[1].string,\
                brand=data[2].string, sellday=data[3].string)
    return text

if __name__ == "__main__":
    out = open('ergtitle.txt','wt',encoding='UTF-8')
    out.write(make("1995-01-01", False, False))
    out.close()