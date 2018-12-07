import config
import json
import os
import traceback

TYPE = 'MESSAGE'
HOOK = 'd'
HELP = config.H(HOOK, " [set|cp|del] [name] (value): Save and load data for ease of access")

if os.path.exists("data/userdata.json"):
    udb = json.load(open("data/userdata.json"))
else:
    udb = {}

def SaveUDB():
    json.dump(udb, open("data/userdata.json", "w"))

def Main(self, line, user):
    print udb
    try:
        if len(line) == 5:
            return udb[user][line[4]]
        elif line[4] == "set":
            udb.setdefault(user, {})
            udb[user][line[5]] =" ".join(line[6:])
            SaveUDB()
            return "Value %s set to '%s'" % (line[5], " ".join(line[6:]))
        elif line[4] == "cp":
            udb.setdefault(user, {})
            udb[user][line[6]] = udb[user][line[5]]
            SaveUDB()
            return "Value copied"
        elif line[4] == "del":
            udb.setdefault(user, {})
            del udb[user][line[5]]
            SaveUDB()
            return "Value '%s' deleted" % line[5]
    except:
        print traceback.print_exc()
