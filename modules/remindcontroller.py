import json
import time
import os

TYPE = "CONSTANT"

def Main(self):
    if os.path.isfile("data/alerts.json"):
        with open("data/alerts.json") as f:
            self.data['alerts'] = json.load(f)
    else:
        with open('data/alerts.json', 'w') as f:
            json.dump({}, f)
            f.close()
        self.data['alerts'] = {}
    for key, timers in self.data['alerts'].iteritems():
        for tup in xrange(len(timers)):
            tup -= 1
            if timers[tup][0] <= time.time():
                print timers
                if self.quiet:
                    self.SendMsg(key, key + ': ' + timers[tup][2])
                else:
                    self.SendMsg(timers[tup][1], key + ': ' + timers[tup][2])
                del timers[tup]
                with open("data/alerts.json", 'w') as f:
                    json.dump(self.data['alerts'], f)

