import config
import random

TYPE = 'MESSAGE'
HOOK = 'eightball'
HELP = config.H(HOOK, ": Get a response from the eightball")

eightball = ['Yes', 'No', 'Maybe', 'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

def Main(self, line, user):
    return random.choice(eightball)