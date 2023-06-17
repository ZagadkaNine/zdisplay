#!/usr/bin/python3

import re

def getLidState():
    if os.path.exists("/proc/acpi/button/lid/LID0/state"):
        f = open("/proc/acpi/button/lid/LID0/state", 'r')
        lidState = re.sub(r"state:[\n\t\s]+", "", f.read()).rstrip()
        f.close()
        return lidState
    return "unknown"


if __name__ == "__main__":
    print("{}".format(getLidState()))
