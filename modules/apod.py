import urllib2
from bs4 import BeautifulSoup
import config

TYPE = 'MESSAGE'
HOOK = "apod"
HELP = config.PREFIX+"apod: Returns the Astronomy Picture of the Day"


def Main(self, line, user):
    parsed = BeautifulSoup(urllib2.urlopen('https://apod.nasa.gov/apod/astropix.html').read(), 'lxml')
    return "\x02"+parsed.find("b").text.strip().rstrip() + "\x02: https://apod.nasa.gov/apod/" + parsed.find('img')['src']
