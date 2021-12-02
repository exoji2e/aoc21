#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 2
def get_year(): return 2021

def p1(v):
    lines = get_lines(v)
    x, y = 0, 0
    for l in lines:
        d, no = lazy_ints(l.split())
        if d[0] == 'f':
            x += no
        if d[0] == 'd':
            y += no
        if d[0] == 'u':
            y -= no
    return x*y

def p2(v):
    lines = get_lines(v)
    x, y = 0, 0
    aim = 0
    for l in lines:
        d, no = lazy_ints(l.split())
        if d[0] == 'f':
            x += no
            y += no*aim
        if d[0] == 'd':
            aim += no
        if d[0] == 'u':
            aim -= no
    return x*y


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
