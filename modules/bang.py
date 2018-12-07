"""irc bangs, instant answers, quick. Credit to NotDavid"""
import urllib
import urllib2
import json
import config
import traceback

TYPE = 'NOHOOK'
#HOOK = "!"
#HELP = config.PREFIX+"! <query>: Searches DuckDuckGo"


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
        print traceback.print_exc()
        return None

def bang(query):
    #line should start with !!
    j = search(query[1:])
    if j == None:
        return "Search failed"
    return j['Redirect']

def Main(self, line, user):
    if line[3][:2] == "!!":
        self.SendMsg(line[2], bang(" ".join([x for x in line[3:]])))
