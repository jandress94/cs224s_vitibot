from bs4 import BeautifulSoup
import re
import urllib
import requests

def get_blurb(id_string):
    url = 'http://www.wine.com/V6/winefoodpairing.aspx?N=%s&show=true' % (id_string)

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,  "html5lib")

    blurb = soup.find(id="ctl00_BodyContent_ctrResults_pnlMessage")
    if blurb is None:
        return None

    return blurb.get_text().strip()

if __name__=='__main__':
    print(get_blurb('7155+3042'))
    print(get_blurb('7155+3104'))
    print(get_blurb('7155+3008'))

    with open('./FoodPairings.py') as pair_file:
        lines = [line for line in pair_file]

    with open('./FoodPairings.py', 'w') as pair_file:
        for line in lines:
            pair_file.write(line)

            stripped_line = line.strip()
            if stripped_line.startswith("'id': "):

                pair_id = stripped_line.split(':')[1].strip()
                if pair_id.startswith('None'): continue
                pair_id = pair_id.split("'")[1]

                blurb = get_blurb('7155+' + pair_id)
                if blurb is not None:
                    print(pair_id)
                    pair_file.write("%s'blurb': '%s',\n" % (line.split("'")[0], blurb))