import config
import random

blames = ['jews', 'government', 'hillary', 'cloud computing', 'trump', 'schools',
        'sjws', 'guns', 'Mexican', 'Canada', 'liberals', 'cuckservatives', 'videogames',
        'muslims', 'communists', 'tv', 'censorship', 'she', 'fatties', 'reddit', '9/11',
        'Obama', '"urbans"', 'hippies', 'corporations', 'hitler', 'illuminati', 'CSI',
        'FOX_News', 'Scientology', 'rethuglikkans', 'Starbucks', 'piracy', 'ISIS',
        'imperialism', 'immigrants', 'China', 'Jesus', 'MexicanJesus', 'vaccines',
        'Mick', 'aliens', 'FuzzyWords', 'gluten']

TYPE = 'MESSAGE'
HOOK = "wob"
HELP = config.H(HOOK, ": Find out who to blame")

def Main(self, line, user):
    self.SendMsg(line[2], "It's time to play! WHEEL! OF! \x02BLAME!")
    return "\x02"+str(random.choice(blames))