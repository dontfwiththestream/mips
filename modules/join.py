import config

TYPE = 'MESSAGE'
HOOK = "join"
HELP = config.PREFIX+"join <channel>: Joins the specified channel"


def Main(self, line, user):
    if user == config.OWNER:
        self.SendData("JOIN " + line[4])