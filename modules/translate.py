import googletrans
import config

t = googletrans.Translator()

TYPE = 'MESSAGE'
HOOK = "t"
HELP = config.H(HOOK, " <foreign language>: Translates the inputted text into English.")

def Main(self, line, user):
    return "<"+user+"> "+" ".join([x.text for x in t.translate(line[4:])])
