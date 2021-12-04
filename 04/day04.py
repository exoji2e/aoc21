#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 4
def get_year(): return 2021

def test(board, used):
    for i in range(5):
        r = board[i]
        if len(set(r) & used) == 5: return True
        c = [board[j][i] for j in range(5)]
        if len(set(c) & used) == 5: return True

    return False

def left(board, used):
    sm = 0
    for r in board:
        for v in r:
            if v not in used:
                sm += v
    return sm

def parse(v):
    chunks = v.split('\n\n')
    items = lazy_ints(chunks[0].split(','))
    boards = []
    for g in chunks[1:]:
        b = [[0]*5 for _ in range(5)]
        lns = g.split('\n')
        for i, line in enumerate(lns):
            b[i] = lazy_ints(line.split())
        boards.append(b)
    return items, boards


def p1(v):
    used = set()
    items, boards = parse(v)
    for v in items:
        used.add(v)
        for board in boards:
            if test(board, used):
                return v * left(board, used)

def p2(v):
    chunks = v.split('\n\n')
    used = set()
    items, boards = parse(v)
    for v in items:
        used.add(v)
        w = []
        l = []
        for board in boards:
            if test(board, used):
                w.append(board)
            else:
                l.append(board)
        if len(l) == 0:
            return v * left(w[0], used)
        boards = l


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
