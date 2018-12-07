import socket
import imp
import os
import traceback
import sys
import random
import select
import time
from config import *
sys.dont_write_bytecode = True
class Main(object):

    def __init__(self):
        self.s = socket.socket()
        self.hooks = {}
        self.help = {}
        self.hookless = []
        self.constant = []

        self.data = {}
        self.quiet = False

        if NICKSERV:
            try:
                self.nspass = NSPASS
            except:
                self.nspass = sys.argv[1]

        self.LoadAll()
        self.InitializeIRC()
        self.IRCLoop()

    def InitializeIRC(self):
        self.s.connect(SERVER)
        self.SendData("NICK "+NICK)
        self.SendData("USER MIPS . . :"+random.choice(TAGLINES))

    def IRCLoop(self):
        b = ""
        while 1:
            time.sleep(0.05)
            sel = select.select([self.s], [], [], 0)
            if self.s in sel[0]:
                b += self.s.recv(1024)
                t = b.split("\n")
                b = t.pop()
                for line in t:
                    print line
                    try:
                        line = line.rstrip().split()
                        if line[0] == "PING":
                            self.SendData("PONG "+line[1])
                            continue
                        elif line[1] in ("376", "422"):
                            self.SendData("MODE " + NICK + " +B")
                            if NICKSERV:
                                self.SendMsg("NickServ", "IDENTIFY "+self.nspass)

                            for chan in CHANS:
                                self.SendData("JOIN "+chan)
                            continue
                        user = line[0].replace(":", '').split("!")[0]
                        line[3] = line[3].replace(":",'')
                        if self.quiet:
                            sendto = user
                        else: sendto = line[2]

                        for func in self.hookless:
                            func(self, line, user)
                        if line[3] in self.hooks.keys():
                            run = self.hooks[line[3]](self, line, user)
                            if run is not None:
                                self.SendMsg(sendto, run)
                        elif line[3] == PREFIX+"help":
                            if random.randrange(1, 100) == 50:
                                self.SendNotice(user, "fuck off, weakling")
                            else:
                                try:
                                    self.SendNotice(user, self.help[line[4].strip(PREFIX)])
                                except IndexError:
                                    self.SendNotice(user, "Commands available: ('"+PREFIX+"help <command>' to get more information)")
                                    self.SendNotice(user, ", ".join(self.hooks))
                        elif user == OWNER and line[3] == PREFIX + "reload":
                            self.LoadAll()
                            self.SendMsg(line[2], "Reloaded!")
                        elif user == OWNER and line[3] == PREFIX + "quiet":
                            self.quiet = not self.quiet
                    except IndexError: pass
                    except: print traceback.print_exc()
            else:
                for constant in self.constant:
                    constant(self)

    def SendMsg(self, chan, text):
        self.SendData(u"PRIVMSG %s :%s" % (chan, text))

    def SendNotice(self, user, text):
        self.SendData(u"NOTICE %s :%s" % (user, text))

    def SendData(self, text):
        self.s.send(u"%s\r\n".encode("utf8") % text[:600].encode("utf8"))

    def LoadAll(self):
        self.hooks = {}
        self.hookless = []
        self.constant = []
        for filename in os.listdir("modules"):
            mod = imp.load_source('mod', "modules/"+filename)

            if mod.TYPE == "MESSAGE":
                self.hooks[PREFIX+mod.HOOK] = mod.Main
                self.help[mod.HOOK] = mod.HELP
                del mod.HOOK
                print "[DEBUG] Loading (Message): " + filename
            elif mod.TYPE == "NOHOOK":
                self.hookless.append(mod.Main)
                print "[DEBUG] Loading (hookless): " + filename
            elif mod.TYPE == "CONSTANT":
                self.constant.append(mod.Main)
                print "[DEBUG] Loading (constant): " + filename


if __name__ == '__main__':
    Main()
