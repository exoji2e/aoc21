#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 8
def get_year(): return 2021

from itertools import permutations

def fix(s):
    return ''.join(sorted(s))

def match(dgs2, my_dgs):
    sols = []
    for p in permutations('abcdefg'):
        mapping = {}
        for dg in my_dgs:
            my_s = []
            for l in dg:
                my_s.append(p[ord(l) - ord('a')])
            D = fix(my_s)
            MD = fix(dg)
            if D in dgs2:
                mapping[MD] = dgs2[D]
            else:
                break
        if len(mapping) == len(my_dgs):
            return mapping


def p1(v):
    lines = get_lines(v)
    cnt = 0
    for l in lines:
        X = l.split()
        for th in X[-4:]:
            if len(th) in [2, 3, 4, 7]:
                cnt += 1
    return cnt

def p2(v):
    lines = get_lines(v)
    dgs = {
        0 : 'abcefg',
        1 : 'cf',
        2 : 'acdeg',
        3 : 'acdfg',
        4 : 'bcdf',
        5 : 'abdfg',
        6 : 'abdefg',
        7 : 'acf',
        8 : 'abcdefg',
        9 : 'abcdfg'
    }
    dgs2 = {}
    for k, v in dgs.items():
        dgs2[v] = k
    su = 0
    for l in lines:
        ks, pin = l.split('|')
        my_dgs = ks.split()
        mapping = match(dgs2, my_dgs)
        vs = []
        for v in pin.split():
            v2 = fix(v)
            vs.append(str(mapping[v2]))
        su += int(''.join(vs))
    return su


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
