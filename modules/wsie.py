import config
import random

TYPE = 'MESSAGE'
HOOK = 'wsiet'
HELP = config.H(HOOK, ": Returns what you should eat tonight")

def Main(self, line, user):
    return random.choice(['pizza', 'popcorn', 'chicken', 'a dick', 'beef', 'salad', 'tofu', 'a hamburger', 'pussy', 'cock', 'jizz', 'cheese', 'cheeseburger', 'penis', 'a man'])