import random
import config

TYPE = 'MESSAGE'
HOOK = "roll"
HELP = config.PREFIX+"roll <N>d<X>: Rolls N X-sided dice"



def Main(self, line, user):
    l = []
    ret = user+": "
    amt = int(line[4].lower().split('d')[0])
    m = int(line[4].lower().split('d')[1])
    if amt < 30 and m < 10000000:
        for x in xrange(amt):
            l.append(str(random.randrange(0,m)))
        return ret+", ".join(l)
    else:
        return "Numbers too high."
