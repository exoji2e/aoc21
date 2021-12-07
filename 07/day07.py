#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 7
def get_year(): return 2021

def minS(v, func):
    ints = lazy_ints(v.split(','))
    ints.sort()
    MIN = 10**10
    for p in range(ints[0], ints[-1] + 1):
        su = 0
        for v in ints:
            d = abs(v - p)
            su += func(d)
        MIN = min(MIN, su)
    return MIN



def p1(v):
    return minS(v, lambda d: d)

def p2(v):
    return minS(v, lambda d: d*(d+1)//2)


if __name__ == '__main__':
    """
    cmds = [
        'run1', 'run2',
        #'print_stats',
        #'submit1',
        #'submit2']
    """
    cmds = get_commands()
    print('Commands:', cmds)
    if 'run_samples' in cmds or 'samples_only' in cmds:
        run_samples(p1, p2, cmds, __file__)
    if 'samples_only' not in cmds:
        run(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
