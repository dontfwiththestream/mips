import config

TYPE = 'MESSAGE'
HOOK = "part"
HELP = config.PREFIX+"part <channel>: Leaves the specified channel"


def Main(self, line, user):
    if user == config.OWNER:
        self.SendData("PART " + line[4] + " :Leaving!")
        print "PART " + line[4] + " :Leaving!"