import config

TYPE = 'MESSAGE'
HOOK = "nick"
HELP = config.PREFIX+"nick <channel>: Admin only. Changes nickname."


def Main(self, line, user):
    if user == config.OWNER:
        self.SendData("NICK " + line[4])
