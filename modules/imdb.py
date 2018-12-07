import config
import urllib2
import urllib
import re
from bs4 import BeautifulSoup

TYPE = 'MESSAGE'
HOOK = 'imdb'
HELP = config.H(HOOK, " <query>: Searches IMDB")

def search(term):
    query = "http://www.imdb.com/find?q="+urllib.quote(term, safe='')
    parsed = BeautifulSoup(urllib2.urlopen(query).read(), 'lxml')
    first = parsed.find('td', {'class': 'result_text'}).find('a')['href']
    return "http://www.imdb.com"+first.split('?')[0]

def getinfo(url):
    parsed = BeautifulSoup(urllib2.urlopen(url).read(), 'lxml')

    return {'title': parsed.find('h1', {'itemprop':'name'}).text.strip(),
    'rating': parsed.find('span', {'itemprop': 'ratingValue'}).text,
    'duration': parsed.find('time', {'itemprop':'duration'}).text.strip().rstrip(),
    'genre': parsed.find('span', {'itemprop':'genre'}).text,
    'date': parsed.find('meta', {'itemprop':'datePublished'})['content']
    }

def Main(self, line, user):
    imdburl = search(" ".join(line[4:]))
    imdbinfo = getinfo(imdburl)
    retstr = imdbinfo['title'] + ' | ' + imdbinfo['rating'] + '/10 | ' + imdbinfo['genre'] + ' | ' + imdbinfo['duration'] + ' | ' + imdbinfo['date'] + ' | ' + imdburl
    return re.sub(r'[^\x00-\x7F]+',' ', retstr)