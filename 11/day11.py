#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 11
def get_year(): return 2021

R, C = 10, 10
def step(G):
    nines = set()
    q = []
    for i in range(R):
        for j in range(C):
            G[i][j] += 1
            if G[i][j] > 9:
                q.append((i, j))
                nines.add((i, j))
    while q:
        q2 = []
        for ii, jj in q:
            for ni, nj in grid8nf(ii, jj, R, C):
                if (ni, nj) in nines: continue
                G[ni][nj] +=1 
                if G[ni][nj] > 9:
                    q2.append((ni, nj))
                    nines.add((ni, nj))
        q = q2
    
    for i, j in nines:
        G[i][j] = 0
    return len(nines), G



def show(G):
    for i in range(R):
        print(''.join(map(str,G[i])))

def p1(v):
    lines = get_lines(v)
    G = [[int(ch) for ch in line] for line in lines]
    ans = 0
    for _ in range(100):
        c, G = step(G)
        ans += c
    return ans

def p2(v):
    lines = get_lines(v)
    G = [[int(ch) for ch in line] for line in lines]
    i = 1
    while True:
        c, G = step(G)
        if c == 100:
            return i
        i += 1

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
