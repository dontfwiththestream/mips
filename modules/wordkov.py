import config
import string
import random


TYPE = 'MESSAGE'
HOOK = 'word'
HELP = config.H(HOOK, " {min length}: Generate a word. Minimum length must be less than 6.")

class WordGen(object):
    def __init__(self, worddb):
        self.db = {}
        for x in self.genalphadict():
            self.db[x] = {'prev': self.genalphadict(), 'next': self.genalphadict(), 'start': 0, 'end': 0}
        self.builddb(worddb)

    def neighborhood(self, iterable):
        iterator = iter(iterable)
        prev_item = None
        current_item = next(iterator)
        for next_item in iterator:
            yield (prev_item, current_item, next_item)
            prev_item = current_item
            current_item = next_item
        yield (prev_item, current_item, None)

    def genalphadict(self):
        alphadict = {}
        for x in list(string.ascii_lowercase):
            alphadict[x] = 0
        alphadict["'"] = 0
        return alphadict

    def builddb(self, dictpath):
        with open(dictpath) as f:
            words = f.readlines()

        for x in words:
            x = x.rstrip().lower().decode('unicode_escape').encode('ascii','ignore')

            split = list(x)
            for l in self.neighborhood(split):
                if l[0] == None:
                    self.db[l[1]]['start'] += 1
                else:
                    self.db[l[1]]['prev'][l[0]] += 1
                if l[2] == None:
                    self.db[l[1]]['end'] += 1
                else:
                    self.db[l[1]]['next'][l[2]] += 1

    def Generate(self, minlen=5, proper=False, doubles=True):
        while 1:
            returnstr = ""
            initlist = []
            for letter in self.db.keys():
                for x in xrange(self.db[letter]['start']):
                    initlist.append(letter)
            initletter = random.choice(initlist)
            returnstr += initletter
            prevletter = initletter
            while 1:
                chance = []
                for letter in self.db[prevletter]['next'].keys():
                    for x in xrange(self.db[prevletter]['next'][letter]):
                        chance.append(letter)
                    for x in xrange(self.db[prevletter]['end'] / 3):
                        chance.append('END')
                nextl = random.choice(chance)
                if nextl == 'END':
                    if len(returnstr) < minlen:
                        pass
                    else:
                        break
                else:
                    returnstr += nextl
                    prevletter = nextl
            if doubles == False:
                for l in self.neighborhood(list(returnstr)):
                    if l == (l[1], l[1], l[1]):
                        returnstr = returnstr.replace(l[1] * 3, l[1])

            if proper:
                if any(x in ['a','e','i','o','u'] for x in list(returnstr)):
                    break
                else:
                    pass
            else:
                break

        return returnstr

    def Generator2(self, minlen=5):
        l = random.choice(list(string.ascii_lowercase))
        initial = l
        returnstr = l
        # handle behind the word
        while 1:
            choice = []
            for x in self.db[l]['prev']:
                for y in xrange(self.db[l]['prev'][x]):
                    choice.append(x)
                for y in xrange(self.db[l]['start'] / 3):
                    choice.append('START')
            letter = random.choice(choice)
            if letter == 'START':
                if len(returnstr) > minlen/2:
                    break
                else:
                    continue
            returnstr = letter + returnstr
            l = letter
        #handle after the letter
        l = initial
        while 1:
            choice = []
            for x in self.db[l]['prev']:
                for y in xrange(self.db[l]['next'][x]):
                    choice.append(x)
                for y in xrange(self.db[l]['end'] / 3):
                    choice.append('END')
            letter = random.choice(choice)
            if letter == 'END':
                if len(returnstr) > minlen:
                    break
                else:
                    continue
            returnstr += letter
            l = letter
        return returnstr


m = WordGen('/usr/share/dict/american-english')

def Main(self, line, user):
    try:
        minlen = int(line[4])
        if minlen > 6:
            minlen = 6
        elif minlen < 0:
            minlen = 0
    except:
        minlen=4
    return m.Generate(minlen=minlen, proper=True)
