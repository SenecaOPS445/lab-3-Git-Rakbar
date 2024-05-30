#!/usr/bin/env python3
#Author_ID: rakbar8

import subprocess

# assign the correct commands into variable

def free_space():
    p = subprocess.Popen(("df -h | grep '/$' | awk '{print $4}'"), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# x = communicate with it? define?
    x = p.communicate()
    space = x[0].decode('utf-8').strip()
    return(space)

print(free_space())