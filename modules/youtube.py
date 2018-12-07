import requests
from bs4 import BeautifulSoup
import traceback
import config

TYPE = 'MESSAGE'
HOOK = "yt"
HELP = config.PREFIX+"yt <query>: Searches youtube for the query"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0 PaleMoon/27.5.1"}


def Main(self, line, user):
    query = "+".join(line[4:])
    req = requests.get("https://www.youtube.com/results?search_query="+query, headers=headers)
    parsed = BeautifulSoup(req.text, "lxml")
    try:
        result = parsed.find("ol", attrs={'class': "item-section"}).find("div", attrs={"class": "yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix"})
        attribs = {
            'title': result.find("a", attrs={"dir": "ltr"})['title'],
            'len': result.find('span', attrs={"class": 'video-time'}).text,
            'url': "https://youtu.be/"+result["data-context-item-id"],
            'uploader': result.find('div', attrs={'class': "yt-lockup-byline"}).text,
            'views': result.find("ul", attrs={'class': 'yt-lockup-meta-info'}).find_all("li")[-1].text,
            'date': result.find("ul", attrs={'class': 'yt-lockup-meta-info'}).find_all("li")[0].text
        }
        return user + ": \x02" + attribs['title'] + "\x02 - " + attribs['len'] + ' - \x02' + attribs['uploader'] + "\x02 - " + attribs['date'] + '\x02 - ' + attribs['views'] + "\x02 - " +attribs['url']
    except:
        print traceback.print_exc()
        return "No results/error"
