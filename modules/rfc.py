import requests
import config
from bs4 import BeautifulSoup

TYPE = 'MESSAGE'
HOOK = "rfc"
HELP = config.PREFIX+"rfc <number>: Returns the specified RFC"

def Main(self, line, user):
    line[4]
    try:
        rfcraw = requests.get('https://tools.ietf.org/html/rfc' + str(int(line[4])))
    except:
        return
    if rfcraw.status_code == 200:
        try:
            rfc = BeautifulSoup(rfcraw.text, 'lxml')
            rfctitle = rfc.find('span', {'class': 'h1'}).text
            return 'https://tools.ietf.org/html/rfc' + str(int(line[4])) + ' - RFC' + str(int(line[4])) + ': ' + rfctitle
        except:
            return 'Something went wrong, but I don\'t want to talk about it.'
    else:
        return 'Requested RFC does not exist.'
