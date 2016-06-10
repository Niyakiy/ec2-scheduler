#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import TimeRanges
import EC2Interface

if __name__ == '__main__':
    a = "21:50-23:25,9:00-11:00,6:00-8:00,0:00-7:00,2:00-4:00,6:00-7:00,6:30-7:00,14:00-20:00,19:00-22:00,23:15-23:30"
    #a = "00:15-00:45,00:46-01:45,00:20-00:50"
    a = "0:0-24:59"
    tr = TimeRanges.TimeRanges(a)

    if tr.validate_and_parse():
        print(tr)
    else:
        print("Invalid ranges")

    #ec2 = EC2Interface.EC2Interface()
    #ec2.connect()
    #ec2.load_ec2_regions()

    #print(ec2.regions)
