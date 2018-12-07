import config

TYPE = 'MESSAGE'
HOOK = "radio"
HELP = config.H(HOOK, ": Reports radio information")

def Main(*args, **kwargs):
    return "Radio is live at http://hoppy.haus:8000/"