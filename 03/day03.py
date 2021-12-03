#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 3
def get_year(): return 2021

def p1(v):
    chunks = v.split('\n\n')
    lines = get_lines(v)
    cnt = Counter()
    sz = len(lines)
    for l in lines:
        for i, ch in enumerate(l):
            if ch == '1': cnt[i] += 1
    gamma = ['1' if cnt[i] > sz//2 else '0' for i in range(len(lines[0]))]
    eps = ['0' if cnt[i] > sz//2 else '1' for i in range(len(lines[0]))]
    g1 = int(''.join(gamma), 2)
    g2 = int(''.join(eps), 2)


    return g1*g2

def p2(v):
    chunks = v.split('\n\n')
    lines = get_lines(v)
    cnt = Counter()
    sz = len(lines)
    things = list(lines)
    for i in range(len(things[0])):
        if len(things) == 1: break
        ones = []
        zeros = []
        for l in things:
            if l[i] == '1': ones.append(l)
            else: zeros.append(l)
        if len(ones) >= len(zeros): 
            things = ones
        else:
            things = zeros
    ogr = int(things[0], 2)
    things = list(lines)
    for i in range(len(things[0])):
        if len(things) == 1: break
        ones = []
        zeros = []
        for l in things:
            if l[i] == '1': ones.append(l)
            else: zeros.append(l)
        if len(ones) >= len(zeros):
            things = zeros
        else:
            things = ones
    co2 = int(things[0], 2)
    return ogr*co2


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
