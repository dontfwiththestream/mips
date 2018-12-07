import config
"""irc bangs, instant answers, quick. Credit to Notdavid"""
import urllib
import urllib2
import json

TYPE = 'MESSAGE'
HOOK = "a"
HELP = config.PREFIX+"a <query>: Searches a DuckDuckGo answer"

def search(query):
    useragent = "chicanery"
    params = {
        'q': query,
        'format': 'json',
        'pretty': '1',
        'no_redirect': '1',
        'no_html': '1',
        'skip_disambig': '1',
    }
    enc_params = urllib.urlencode(params)
    url = 'http://api.duckduckgo.com/?' + enc_params
    try:
        request = urllib2.Request(url, headers={'User-Agent': useragent})
        response = urllib2.urlopen(request)
        j = json.loads(response.read())
        response.close()
        return j
    except Exception:
        return None

def answer(query):
    #line should start with "!a", which should be stripped
    j = search(query)
    if j == None:
        return "Search failed"
    return j['Answer']

def Main(self, line, user):
    return answer(" ".join(line[4:]))
