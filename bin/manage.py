#!/usr/bin/python3

from lid_status import getLidState

import syslog

if __name__ == "__main__":
    syslog.syslog(syslog.LOG_INFO, "Lid state: {}".format(getLidState()))
    print("{}".format(getLidState()))


