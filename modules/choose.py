import config
import random

TYPE = 'MESSAGE'
HOOK = "choose"
HELP = config.H(HOOK, " <space-separated terms>: Chooses a random term.")

def Main(self, line, user):
    return random.choice(line[4:])