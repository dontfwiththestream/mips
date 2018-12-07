import config
import json
import urllib2

TYPE = 'MESSAGE'
HOOK = "crypto"
HELP = config.PREFIX+"crypto <currency abbreviation>: Reports the price for the specified (crypto)currency"

def Main(self, line, user):
    try:
        mul = float(line[5])
    except (IndexError, ValueError, TypeError):
        mul = 1.0
    currency = json.loads(urllib2.urlopen('https://min-api.cryptocompare.com/data/price?fsym=' + line[4].upper() + '&tsyms=USD,EUR,NZD,CAD').read())
    retstr = "Value of "+line[4].upper()+': '+", ".join([str(value * mul)+' '+abb for abb, value in currency.iteritems()])
    return retstr