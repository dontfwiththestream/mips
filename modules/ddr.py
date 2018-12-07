import config
import time
import json
import os
import random

TYPE = "CONSTANT"

class Controller(object):
    def __init__(self):
        self.current = ""
        self.interval = 30
        self.endtime = 0
        self.ic = 0 #ooooh boy

        self.active = False

        if os.path.exists("data/ddr.json"):
            with open('data/ddr.json') as f:
                self.points = json.load(f)
        else:
            self.points = {}

    def Save(self):
        with open('data/ddr.json', 'w') as f:
            json.dump(self.points, f)

    def GenerateDDR(self):
        self.current = ""
        for x in xrange(20):
            self.current += random.choice('uldr')
        return self.current

    def GetPoints(self, msg, user):
        t = time.time()
        pts = 0
        accuracy = 0
        for m in xrange(len(msg)):
            if msg[m] == self.current[m]:
                pts += 1
                accuracy += 1

        if accuracy < 15: return False
        pts *= (30 - (int(t) % 30)) / 2
        tim = int(t) % 30
        if tim < 5: return ""
        acc = accuracy / 0.2
        self.points[user.lower()] = self.points.setdefault(user.lower(), 0) + pts
        self.Save()
        return pts, int(tim), int(acc)



def Main(self):
    self.data['ddr'] = self.data.setdefault('ddr', Controller())
    if self.data['ddr'].ic > int(time.time()) % 30:
        self.data['ddr'].ic = int(time.time()) % 30
        self.SendMsg('#ddr', u"\u200b".join(self.data['ddr'].GenerateDDR()))
        self.data['ddr'].active = True
    else:
        self.data['ddr'].ic = int(time.time()) % 30
