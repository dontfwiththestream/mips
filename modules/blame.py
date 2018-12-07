import config

TYPE = 'MESSAGE'
HOOK = 'blame'
HELP = config.H(HOOK, " <user>: Blame the specified user")

def Main(self, line, user):
    return line[4] + " did it!"
