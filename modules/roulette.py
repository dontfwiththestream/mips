import config
import random

TYPE = 'MESSAGE'
HOOK = "roulette"
HELP = config.H(HOOK, ": If the bot is OP, kick on a 1/6 chance")

def Main(self, line, user):
    if random.randrange(0, 6) == 4:
    	self.SendData("KICK %s %s BANG" % (line[2], user))
    else:
        return "*click*"
