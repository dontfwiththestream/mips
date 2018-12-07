import json
import os
import traceback

TYPE = "NOHOOK"
if not os.path.isdir("data"):
    os.mkdir("data")

def Main(self, line, user):
    if os.path.isfile("data/messages.json"):
        with open("data/messages.json") as f:
            self.data['mail'] = json.load(f)
    else:
        with open('data/messages.json', 'w') as f:
            json.dump({}, f)
            f.close()
        self.data['mail'] = {}
    try:
        luser = user.lower()
        if luser in self.data['mail'].keys():
            for msg in self.data['mail'][luser]:
                self.SendMsg(line[2], user+" "+msg)
            del self.data['mail'][luser]
            with open('data/messages.json', 'w') as f:
                json.dump(self.data['mail'], f)
                f.close()
    except KeyError:
        print traceback.print_exc()
