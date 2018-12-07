import config

TYPE = 'NOHOOK'

def Main(self, line, user):
    line[3] = line[3].replace(':', '')
    if line[2].lower() == "#ddr" and self.data['ddr'].active:
        print repr(line[3])
        if all(c in "udlr" for c in line[3]):
            print 'triggered'
            pts = self.data['ddr'].GetPoints(line[3], user)
            if not pts and pts != "":
                 self.SendMsg("#ddr", "Accuracy too low!")
            if not pts and pts == "":
                 self.SendMsg("#ddr", "Hmmmmmmmm")
            else:
                self.SendMsg('#ddr', str(pts[0])+" points to "+user+", who had an accuracy of "+str(pts[2])+"% in "+str(pts[1])+" seconds! "+user+" now has "+str(self.data['ddr'].points[user.lower()])+'.')
                self.data['ddr'].active = False
