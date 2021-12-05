#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 5
def get_year(): return 2021

def parse(line):
    x, y, _, x2, y2 = line.replace(',', ' ').split()
    return map(int, [x, y, x2, y2])

def p1(v):
    lines = get_lines(v)
    C = Counter()
    for l in lines:
        x1, y1, x2, y2 = parse(l)
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        if x1 == x2:
            yl, yh = min(y1, y2), max(y1, y2)
            for y in range(yl, yh+1):
                C[x1, y] += 1
        elif y1 == y2:
            xl, xh = min(x1, x2), max(x1, x2)
            for x in range(xl, xh+1):
                C[x, y1] += 1

    no = 0
    for v in C.values():
        if v > 1: no += 1

    return no

def p2(v):
    lines = get_lines(v)
    C = Counter()
    for l in lines:
        x1, y1, x2, y2 = parse(l)
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        if x1 == x2:
            yl, yh = min(y1, y2), max(y1, y2)
            for y in range(yl, yh+1):
                C[x1, y] += 1
        elif y1 == y2:
            xl, xh = min(x1, x2), max(x1, x2)
            for x in range(xl, xh+1):
                C[x, y1] += 1
        elif dx == dy:
            gx = 1 if x2 > x1 else -1
            gy = 1 if y2 > y1 else -1
            x, y = x1, y1
            while (x, y) != (x2, y2):
                C[x, y] += 1
                x, y = x + gx, y + gy
            C[x, y] += 1

    no = 0
    for v in C.values():
        if v > 1: no += 1

    return no


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
