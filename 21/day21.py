#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 21
def get_year(): return 2021

def roll(dice, i):
    su = 0
    for _ in range(3):
        su += dice[i]
        i += 1
        i %= len(dice)
    return su, i

def parse(v):
    lines = get_lines(v)
    chunks = v.split('\n\n')
    pos1 = int(lines[0].split()[-1])
    pos2 = int(lines[1].split()[-1])
    return [pos1, pos2]   

def p1(v):
    pos = parse(v)
    dice = [i for i in range(1, 101)]
    points = [0, 0]
    i = 0
    no = 0
    who = 0
    while max(points) < 1000:
        no += 3
        add, i = roll(dice, i)
        pos[who] = (pos[who] + add - 1)%10 + 1
        points[who] += pos[who]
        who ^= 1

    return no*min(points)

def p2(v):
    pos = parse(v)
    DP = {}
    rolls = [1, 2, 3]
    C = Counter()
    for a in rolls:
        for b in rolls:
            for c in rolls:
                C[a + b + c] += 1
    


    def solve(who, pos1, pos2, p1, p2):
        T = who, pos1, pos2, p1, p2
        if T in DP:
            return DP[T]
        if p1 >= 21:
            return (1, 0)
        if p2 >= 21:
            return (0, 1)
        V = [0, 0]
        for k, no in C.items():
            if who == 0:
                np = (pos1 + k - 1)%10 + 1
                w1, w2 = solve(1, np, pos2, p1 + np, p2)
            else:
                np = (pos2 + k - 1)%10 + 1
                w1, w2 = solve(0, pos1, np, p1, p2 + np)
            V[0] += w1*no
            V[1] += w2*no
        DP[T] = V
        return V
    V = solve(0, pos[0], pos[1], 0, 0)
    return max(V)


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
