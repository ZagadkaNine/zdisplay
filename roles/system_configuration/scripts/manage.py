#!/usr/bin/python3

import syslog
import re
import os

def getLidState():
    lidPath = "/proc/acpi/button/lid/LID0/state"
    if os.path.exists(lidPath):
        f = open(lidPath, "r")
        lidState = re.sub(r"state:[\n\t\s]+", "", f.read()).rstrip()
        f.close()
        return lidState
    return "unknown"

if __name__ == "__main__":
    syslog.syslog(syslog.LOG_INFO, "Lid state: {}".format(getLidState()))
    print("{}".format(getLidState()))


