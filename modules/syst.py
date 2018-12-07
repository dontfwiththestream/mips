import config
import os
import psutil
import datetime

TYPE = 'MESSAGE'
HOOK = 'sys'
HELP = config.H(HOOK, ": Returns server stats")

def GetUptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        return str(datetime.timedelta(seconds = uptime_seconds))

def Main(self, line, user):
    load = "CPU: (1m:%f 5m: %f 15m:%f)" % os.getloadavg()
    return load+' RAM: '+str(psutil.virtual_memory().percent)+"% UPTIME: "+GetUptime()
