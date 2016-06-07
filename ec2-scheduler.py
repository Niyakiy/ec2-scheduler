#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import TimeRanges

if __name__ == '__main__':
    a = "21:50-23:25,9:00-11:00,6:00-8:00,0:00-7:00,2:00-4:00,6:00-7:00,6:30-7:00,14:00-20:00,19:00-22:00,23:15-23:30"
    #a = "0:00-1:00,2:00-23:59"
    tr = TimeRanges.TimeRanges(a)

    if tr.validate_and_parse():
        print(tr)
    else:
        print("Invalid ranges")
