import config
import random

lop = open('data/lop.db').read().splitlines()

TYPE = 'MESSAGE'
HOOK = "wop"
HELP = config.H(HOOK, ": Roll the wheel of porn!")

def Main(self, line, user):
    self.SendMsg(line[2], " i present to you")
    self.SendMsg(line[2], " the WHEEEEL OF PORN")
    return "<" + user + '> ' + str(random.choice(lop))