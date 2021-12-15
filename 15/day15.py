#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 15
def get_year(): return 2021


from heapq import heappop as pop, heappush as push
# adj: adj-list where edges are tuples (node_id, weight):
# (1) --2-- (0) --3-- (2) has the adj-list:
# adj = [[(1, 2), (2, 3)], [(0, 2)], [0, 3]]
def dijk(adj, S, T):
    N = len(adj)
    INF = 10**18
    dist = [INF]*N
    pq = []
    def add(i, dst):
        if dst < dist[i]:
            dist[i] = dst
            push(pq, (dst, i))
    add(S, 0)

    while pq:
        D, i = pop(pq)
        if i == T: return D
        if D != dist[i]: continue
        for j, w in adj[i]:
            add(j, D + w)
    
    return dist[T]

def wrap(G, cnt):
    R0, C0 = len(G), len(G[0])
    G2 = [[0 for _ in range(C0*cnt)] for _ in range(R0*cnt)]
    for ir in range(cnt):
        for ic in range(cnt):
            for r in range(R0):
                for c in range(C0):
                    ov = G[r][c]
                    nv = 1 + (ov + ir + ic - 1)%9
                    G2[ir*R0 + r][ic*C0 + c] = nv
    return G2

def solve(v, cnt=1):
    lines = get_lines(v)
    G_0 = [[int(ch) for ch in line] for line in lines]
    G = wrap(G_0, cnt)
    R, C = len(G), len(G[0])
    adj = [[] for _ in range(R*C)]
    for r in range(R):
        for c in range(C):
            id = r*C + c
            for nr, nc in grid4nf(r, c, R, C):
                id2 = nr*C + nc
                adj[id].append((id2, G[nr][nc]))
    dst = dijk(adj, 0, len(adj)-1)
    return dst

def p1(v):
    return solve(v)

def p2(v):
    return solve(v, 5)


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
