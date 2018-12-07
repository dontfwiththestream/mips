import config

TYPE = 'MESSAGE'
HOOK = 'raq'
HELP = config.H(HOOK, ": Is peaceful. If the prefix is anything other than !, the joke is lost.")

def Main(self, line, user):
    return "Allahu Akbar"