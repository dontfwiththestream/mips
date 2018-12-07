import config
import re
import time
import json
import os

TYPE = 'MESSAGE'
HOOK = 'remind'
HELP = config.H(HOOK, " <time (5s, 1m, 24hr, 3d)> <message>: Reminds you in the specified amount of time")


def ParseTime(s):
    amt = int(re.sub(r'[a-z]', '', s.lower()))
    t = re.search(r'([a-z][a-z]?)', s.lower()).group(1)
    times = {
        'd': lambda: amt*24*60*60,
        'hr': lambda: amt*60*60,
        'm': lambda: amt*60,
        's': lambda: amt,
    }
    if t not in times.keys() or amt <= 0 or amt >= 999:
        raise IndexError
    else:
        return time.time() + times[t]()


def Main(self, line, user):
    if os.path.isfile("data/alerts.json"):
        with open("data/alerts.json") as f:
            self.data['alerts'] = json.load(f)
    else:
        with open('data/alerts.json', 'w') as f:
            json.dump({}, f)
            f.close()
            self.data['alerts'] = {}
    self.data['alerts'][user] = self.data['alerts'].setdefault(user, [])
    self.data['alerts'][user].append((ParseTime(line[4]), line[2], " ".join(line[5:])))
    with open("data/alerts.json", 'w') as f:
        json.dump(self.data['alerts'],f)
    return user + ": Alert set."
