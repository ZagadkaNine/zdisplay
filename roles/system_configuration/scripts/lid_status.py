#!/usr/bin/python3

import re

def getLidState():
    f = open("/proc/acpi/button/lid/LID0/state", 'r')
    lidState = re.sub(r"state:[\n\t\s]+", "", f.read()).rstrip()
    f.close()
    return lidState

if __name__ == "__main__":
    print("{}".format(getLidState()))
