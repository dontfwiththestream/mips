import config
import requests

TYPE = 'MESSAGE'
HOOK = "drug"
HELP = config.H(HOOK, " <drug>: Searches the Psychonaut wiki for the specified drug.")


def Main(self, line, user):
    headers = {'User-Agent': 'DrugBot/1.0'}
    query = requests.get(
        'https://psychonautwiki.org/w/api.php?action=opensearch&limit=10&namespace=0&format=json&search=' + " ".join(line[4:]), headers=headers)
    results = query.json()
    return user + ", " + results[3][0]