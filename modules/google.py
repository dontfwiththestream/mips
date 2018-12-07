import requests
import traceback
import config
from bs4 import BeautifulSoup

TYPE = 'MESSAGE'
HOOK = "g"
HELP = config.PREFIX+"g <query>: Searches google for your query"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0 PaleMoon/27.5.1"}

def Main(self, line, user):
    try:
        r = requests.get("https://www.google.com/search?q=test"+"+".join(line[4:]), headers=headers).text
        parsed = BeautifulSoup(r, 'lxml')
        result = parsed.find("div", attrs={'class': 'g'})
        title = result.find("h3", attrs={'class':'r'}).find('a')
        return user + ': ' + title['href'] + ' - \x02' + title.text + '\x02 - ' + result.find("span", attrs={"class": "st"}).text
    except:
        print traceback.print_exc()
        return "No results/error"