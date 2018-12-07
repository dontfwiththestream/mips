import re
import config
cache = {}

TYPE="NOHOOK"

def Parse(raw, chan):
    spl = [x for x in re.split(r'(?<!\\)/', raw[2:]) if x]
    print spl
    if len(spl) < 2:
        return
    else:
        cache.setdefault(chan, [])
        for l in cache[chan]:
            if spl[0] in l[1]:
                return (l[0],l[1].replace(spl[0], "\x02%s\x02"%spl[1].replace("\x02", '')))
        return

def Main(self, line, user):
    if line[3][:2].lower() == "s/":
        sed = Parse(" ".join(line[3:]), line[2])
        if sed:
            self.SendMsg(line[2], "Correction, <%s> %s"%(sed[0], sed[1]))
            cache[line[2]].insert(0, (sed[0], sed[1]))
            if len(cache[line[2]]) == 10: cache[line[2]].pop()
    elif line[1] == "PRIVMSG":
        cache.setdefault(line[2], [])
        cache[line[2]].insert(0, (user, " ".join(line[3:])))
        if len(cache[line[2]]) == 10: cache[line[2]].pop()
