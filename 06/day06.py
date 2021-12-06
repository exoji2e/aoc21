#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 6
def get_year(): return 2021

def count(v, N):
    ints = lazy_ints(v.split(','))
    C = Counter(ints)
    for i in range(N):
        nxt = Counter()
        for k, v in C.items():
            if k == 0:
                nxt[6] += v
                nxt[8] += v
            else:
                nxt[k-1] += v
        C = nxt
    
    return sum(C.values())


def p1(v):
    return count(v, 80)


def p2(v):
    return count(v, 256)


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
