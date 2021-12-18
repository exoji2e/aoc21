#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 18
def get_year(): return 2021

def walk(L, d):
    if type(L) != list: return 0, None
    #print(L, d)
    if d == 4 and type(L) == list:
        #print(L[0], L[1])
        return 1, (L[0], L[1])
    for i, th in enumerate(L):
        ok, res = walk(th, d+1)
        if ok != 0: break
    if ok != 0:
        a, b = res
        if ok == 1:
            L[i] = 0
        if i - 1 >= 0:
            giveR(L, i-1, a)
            a = None
        if i + 1 < len(L):
            giveL(L, i+1, b)
            b = None
        return 2, (a, b)
    return 0, None
def giveL(L, i, b):
    if b == None: return
    pos = i
    while type(L[pos]) == list:
        L = L[pos]
        pos = 0
    L[pos] += b
def giveR(L, i, b):
    if b == None: return
    pos = i
    while type(L[pos]) == list:
        L = L[pos]
        pos = len(L) - 1
    L[pos] += b

def reduce(curr):
    while True:
        ch, _ = walk(curr, 0)
        if ch: continue
        ch = expand(curr, 0)
        if not ch: break
    return curr

def expand(L, d):
    if type(L) != list: return 0
    for i, th in enumerate(L):
        if expand(th, d+1): return True
        if type(th) == int and th > 9:
            L[i] = [th//2, (th+1)//2]
            return 1
    return 0
def mag(L):
    if type(L) == int: return L
    else:
        return 3*mag(L[0]) + 2*mag(L[1])



def p1(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    nums = []
    mx = 0
    for i, line in enumerate(lines):
        nums.append(eval(line))

    curr = reduce(nums[0])
    for s in nums[1:]:
        curr = [curr, reduce(s)]
        curr = reduce(curr)
    return mag(curr)

def p2(v):
    lines = get_lines(v)
    mx = 0
    for i, line in enumerate(lines):
        for j, line2 in enumerate(lines):
            s1 = reduce(eval(line))
            s2 = reduce(eval(line2))
            mx = max(mag(reduce([s1, s2])), mx)
    return mx


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
