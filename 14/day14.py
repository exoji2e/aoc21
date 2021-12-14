#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 14
def get_year(): return 2021

def calc(v, no):
    chunks = v.split('\n\n')
    p = chunks[0]
    lns = chunks[1].strip().split('\n')
    rules = {}
    r2 = {}
    for l in lns:
        x, y = l.split(' -> ')
        rules[x] = y
    V = Counter()
    for i in range(len(p) - 1):
        x = p[i:i+2]
        V[x] += 1
    V[p[-1]] += 1

    for _ in range(no):
        V2 = Counter()
        for k, v in V.items():
            if k in rules:
                y = rules[k]
                a = k[0] + y
                b = y + k[1]
                V2[a] += v
                V2[b] += v
            else:
                V2[k] += v
        V = V2
    C = Counter()
    for k, v in V.items():
        C[k[0]] += v
    lst = sorted(C.values())
    return lst[-1] - lst[0]

def p1(v):
    return calc(v, 10)

def p2(v):
    return calc(v, 40)


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
