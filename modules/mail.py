import config
import json

TYPE = 'MESSAGE'
HOOK = "mail"
HELP = config.H(HOOK, "<username> <message>: Will send the specified message to the specified user next time they say something. Maximum of 4 messages.")

def Main(self, line, user):
    if not line[5]: raise IndexError
    self.data['mail'][line[4].lower()] = self.data['mail'].setdefault(line[4].lower(), [])
    if len(self.data['mail'][line[4].lower()]) >= 5:
        self.data['mail'][line[4]].pop(0)
    self.data['mail'][line[4].lower()].append("Mail(" + user + '): ' + " ".join(line[5:]).strip().rstrip())
    with open('data/messages.json', 'w') as f:
        json.dump(self.data['mail'], f)
        f.close()
    return "Message sent to "+line[4]