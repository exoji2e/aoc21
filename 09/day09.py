#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 9
def get_year(): return 2021

def neighs(i, j):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

def p1(v):
    lines = get_lines(v)
    grid = [[int(ch) for ch in line] for line in lines]
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            h = grid[i][j]
            ok = True
            for ni, nj in neighs(i, j):
                if ni >= 0 and ni < len(grid) and nj >= 0 and nj <len(grid[i]):
                    ok =  ok and h < grid[ni][nj]
            if ok: ans += h + 1

    return ans

def p2(v):
    lines = get_lines(v)
    grid = [[int(ch) for ch in line] for line in lines]
    lows = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            h = grid[i][j]
            ok = True
            for ni, nj in neighs(i, j):
                if ni >= 0 and ni < len(grid) and nj >= 0 and nj <len(grid[i]):
                    ok =  ok and h < grid[ni][nj]
            lows.append((i, j))
    Ls = []
    for i, j in lows:
        q = [(i, j)]
        seen = set(q)
        while q:
            q2 = []
            for i, j in q:
                for ni, nj in neighs(i, j):
                    if ni >= 0 and ni < len(grid) and nj >= 0 and nj <len(grid[i]):
                        h_new = grid[ni][nj]
                        if h_new != 9 and h_new > grid[i][j]:
                            if (ni, nj) not in seen:
                                seen.add((ni, nj))
                                q2.append((ni, nj))
            q = q2
        Ls.append(len(seen))
    Ls.sort()
    return Ls[-3]*Ls[-2]*Ls[-1]
                            


    

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
