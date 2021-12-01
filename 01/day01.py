#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 1
def get_year(): return 2021

def p1(v):
    lines = get_lines(v)
    L = len(lines)
    numbers = lazy_ints(lines)
    no = 0
    for i in range(1, L):
        if numbers[i-1] < numbers[i]:
            no += 1
    return no

def p2(v):
    lines = get_lines(v)
    L = len(lines)
    numbers = lazy_ints(lines)
    no = 0
    for i in range(3, L):
        s1 = sum(numbers[i-3:i])
        s2 = sum(numbers[i-2:i+1])
        if s1 < s2:
            no += 1
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
