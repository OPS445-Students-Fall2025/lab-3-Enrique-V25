#!/usr/bin/env python3
#Author ID: emolina3

import os 

def free_space():
    freeSpace = os.popen("df -h | grep '/$' | awk '{print $4}'").read().strip()
    return freeSpace
print(free_space())
