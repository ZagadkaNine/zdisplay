#!/usr/bin/python3

import syslog
import re
import os
from Xlib import X, display, Xutil
from Xlib.ext import randr

def get_lid_state():
    lidPath = "/proc/acpi/button/lid/LID0/state"
    if os.path.exists(lidPath):
        f = open(lidPath, "r")
        lidState = re.sub(r"state:[\n\t\s]+", "", f.read()).rstrip()
        f.close()
        return lidState
    return "unknown"

def get_active_randr_outputs():
    d = display.Display()
    s = d.screen()
    window = s.root.create_window(0, 0, 1, 1, 1, s.root_depth)
    res = randr.get_screen_resources(window)
    outputs = []
    for output in res.outputs:
        info = randr.get_output_info(window, output, 0)
        if info.connection == 0:
            print(info)
            outputs.append(info.name)
    return outputs

if __name__ == "__main__":
    syslog.syslog(syslog.LOG_INFO, "Lid state: {}".format(get_lid_state()))
    print("{}".format(get_lid_state()))

    
    displays_names = get_active_randr_outputs() 
    print("{}".format(displays_names))
