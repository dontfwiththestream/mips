import config
import random

TYPE = 'MESSAGE'
HOOK = "confirm"
HELP = config.H(HOOK, " <thing>: Confirms the specified thing")

def Main(self, line, user):
    spline = " ".join(line[4:])
    msg = spline + " is not confirmed, sorry"
    r = random.random()
    if r < 0.01:
        msg = spline + " is confirmed! You can rest in peace now"
    elif r < 0.25:
        msg = spline + " is not confirmed, but we have heard rumor"
    elif r < 0.5:
        msg = spline + " is not confirmed, but we have heard many rumors"
    return msg