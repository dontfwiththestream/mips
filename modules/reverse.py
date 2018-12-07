import config

TYPE = 'MESSAGE'
HOOK = "reverse"
HELP = config.H(HOOK, " <text>: Reverses the specified text.")

def Main(self, line, user):
    return " ".join(line[4:])[::-1]