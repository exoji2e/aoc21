#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 20
def get_year(): return 2021

def extract_no(G, r, c):
    things = []
    cords = set()
    for rr in range(r-1, r+2):
        for cc in range(c-1, c+2):
            things.append('1' if G[rr,cc] == '#' else '0')
            cords.add((rr, cc))
    return int(''.join(things), 2), cords


def conv(G, MAP, R, C, ch):
    G2 = defaultdict(lambda: ch)
    toVisit = set()
    L = list(G.keys())
    for r, c in L:
        _, S = extract_no(G, r, c)
        toVisit |= S
    
    for r, c in toVisit:
        e, _ = extract_no(G, r, c)
        G2[r, c] = MAP[e]
    return G2
            
def P(G, R, C):
    for i in range(-5, R+5):
        line = ''
        for j in range(-5, C+5):
            line += G[i, j]
        print(line)
    print('------------')

def solve(v, rounds=1):
    chunks = v.split('\n\n')
    MAP = ''.join(chunks[0].split())
    G = defaultdict(lambda: '.')
    lns = chunks[1].split()
    R = len(lns)
    C = len(lns[0])
    for i, line in enumerate(lns):
        for j, ch in enumerate(line):
            G[i,j] = ch
    if MAP[0] == '#': assert MAP[-1] == '.'
    swap = MAP[0] == '#'
    for rnd in range(rounds):
        G = conv(G, MAP, R, C, '#' if swap else '.')
        G = conv(G, MAP, R, C, '.')
    no = 0
    for k, v in G.items():
        if v == '#': no += 1

    return no


def p1(v):
    return solve(v)

def p2(v):
    return solve(v, 25)


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
