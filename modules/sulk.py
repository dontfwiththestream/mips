import time
import random
import config

TYPE = "CONSTANT"

quotes = [
    "Life? Don't talk to me about life!",
    "I'd make a suggestion, but nobody listens.",
    "I've been talking to the merkle. It hates me.",
    "This will all end in tears.",
    "Sorry, did I say something wrong? Pardon me for breathing which I never do anyway so I don't know why I bother to say it. Oh God I'm so depressed.",
    "I think you ought to know I'm feeling very depressed.",
    "It gives me a headache just trying to think down to your level.",
    "You think you've got problems. What are you supposed to do if you are a manically depressed robot? No, don't even bother answering. I'm 50,000 times more intelligent than you and even I don't know the answer."]

cooldown = time.time() + random.randint(3600, 36000)

off = False

def Main(self):
    if time.time() > cooldown and not off:
        self.SendMsg(random.choice(config.CHANS), random.choice(quotes))
        global cooldown
        cooldown = time.time() + random.randint(3600, 18000)
