#!/usr/bin/python

import os


def mem_usage():
    f = os.popen("free -m |grep Mem |awk '{print $2,$3,$4}'")
    return f.read().strip()

def swap_usage():
    f = os.popen("free -m |grep Swap |awk '{print $2,$3,$4}'")
    return f.read().strip()


def load_avg():
    f = os.popen("uptime | sed 's/,//g' | awk '{print $8,$9,$10,$11,$12}'")
    return f.read().strip()


def disk_usage():
 #   f = os.popen("df -h | head -2 | awk '{print $2,$3,$4,$5}'")
    f = os.popen("df -h | grep -v Filesystem")
    f = f.read().replace("\n","\?")
        
    return f


def cpu_usage():
    f = os.popen("top -bi -n 1| awk '{print $2,$3,$4,$5}'").read().split('\n')[2]
    return f

