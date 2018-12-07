import config

import math
import string
import re

table = {
    "km": lambda m: str(m*.62)+'mi',
    "mi": lambda m: str(m*1.609344)+'km',
    "m": lambda m: str(m*3.28084)+'ft',
    "ft": lambda m: str(m*0.3048)+'m',
    "in": lambda m: str(m*2.54)+'cm',
    "cm": lambda m: str(m*0.393701)+'in',
    "oz": lambda m: str(m*28.3495)+'g',
    "g": lambda m: str(m*0.035274)+'oz',
    "lb": lambda m: str(m*0.453592)+'kg',
    "kg": lambda m: str(m*2.20462)+'lb',
    "c": lambda m: str((m*1.8) + 32)+'f',
    "f": lambda m: str((m - 32) * .5556)+'c',
}

def Parse(s):
    amt = int("".join([x for x in s if x in string.digits + '-']))
    measure = str("".join([x for x in s.lower() if x in string.ascii_lowercase]))
    return table[measure](amt)

TYPE = 'MESSAGE'
HOOK = 'convert'
HELP = config.H(HOOK, " <amount and unit>: Simple unit conversion.")

def Main(self, line, user):
    return user + ": "+ Parse(line[4])
