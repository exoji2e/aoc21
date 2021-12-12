#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 12
def get_year(): return 2021

def p1(v):
    lines = get_lines(v)
    G = defaultdict(list)
    for l in lines:
        a, b = l.split('-')
        G[a].append(b)
        G[b].append(a)
    q = []
    vis = set()
    def add(e, path, q):
        if e[0].lower() == e[0] and e in path: return
        path2 = path + [e]
        pathstr = ','.join(path2)
        if pathstr in vis: return
        q.append(path2)
        vis.add(pathstr)
    add('start', [], q)
    while q:
        q2 = []
        for s in q:
            u = s[-1]
            for v in G[u]:
                add(v, s, q2)
        q = q2
    no = 0
    for SET in vis:
        if SET[-3:] == 'end':
            no += 1
    return no


def p2(v):
    lines = get_lines(v)
    G = defaultdict(list)
    for l in lines:
        a, b = l.split('-')
        G[a].append(b)
        G[b].append(a)
    q = []
    vis = set()
    def add(e, path, hasD, q):
        if e[0].lower() == e[0] and e in path: 
            if e == 'start' or e == 'end': return
            if hasD: return
            hasD = True
        path2 = path + [e]
        pathstr = ','.join(path2)
        if pathstr in vis: return
        q.append((path2, hasD))
        vis.add(pathstr)
    add('start', [], False, q)
    while q:
        q2 = []
        for s, hasD in q:
            u = s[-1]
            for v in G[u]:
                add(v, s, hasD, q2)
        q = q2
    no = 0
    for SET in vis:
        if SET[-3:] == 'end':
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
