#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 13
def get_year(): return 2021

def fold(G, fold):
    coord, v = lazy_ints(fold.split('='))
    G2 = set()
    if coord[-1] == 'x':
        for x, y in G:
            if x < v:
                G2.add((x, y))
            else:
                G2.add((2*v - x, y))
    else:
        for x, y in G:
            if y < v:
                G2.add((x, y))
            else:
                G2.add((x, 2*v - y))
    return G2

def parse(v):
    chunks = v.split('\n\n')
    G = set()
    for line in chunks[0].split('\n'):
        x, y = lazy_ints(line.split(','))
        G.add((x, y))
    folds = chunks[1].split('\n')
    return G, folds


def p1(v):
    G, folds = parse(v)
    G = fold(G, folds[0])
    return len(G)

def p2(v):
    G, folds = parse(v)
    for line in folds:
        G = fold(G, line)
    maxX = max(G)[0]
    maxY = max(G, key=lambda v: v[1])[1]
    lines = []
    for i in range(maxY+1):
        line = ''
        for j in range(maxX+1):
            if (j, i) in G:
                line += '#'
            else:
                line += ' '
        lines.append(line)
    return '\n' + '\n'.join(lines)


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
