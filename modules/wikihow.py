import urllib2
import config

TYPE = 'MESSAGE'
HOOK = "wikihow"
HELP = config.H(HOOK, ": Returns a random Wikihow article")

def Main(self, line, user):
    return urllib2.urlopen('http://www.wikihow.com/Special:Randomizer').url