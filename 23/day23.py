#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 23
def get_year(): return 2021

targetC = {
    'A': 3,
    'B' : 5,
    'C' : 7,
    'D' : 9
}
COST = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

def getMoves(grid, r, c, R, C):
    thing = grid[r][c]
    if r == 1: # in cooridor!
        col = targetC[thing]
        ok = True
        steps = 0
        row = 1
        if c < col:
            lst = list(range(c+1, col+1))
        else:
            lst = list(range(col, c))
        for cc in lst:
            steps += 1
            if grid[r][cc] != '.':

                ok = False
                break
        if grid[2][col] != '.': 
            ok = False
        for rr in range(2, 6):
            ch = grid[rr][col]
            if ch == '#': break
            if ch != '.' and ch != thing:
                ok = False 
            if ch == '.':
                steps += 1
                row += 1
        if ok:
            #print('ok', thing, r, c, row, col, steps)
            yield row, col, steps
        else:
            pass #print('fail', thing, r, c)

    else: # in shackt
        vis = {}
        q = [(r, c)]
        steps = 0
        while q:
            q2 = []
            steps += 1
            for r2, c2 in q:
                for r3, c3 in grid4nf(r2, c2, R, C):
                    if grid[r3][c3] == '.' and (r3, c3) not in vis:
                        vis[r3, c3] = steps
                        q2.append((r3, c3))
            q = q2
        for (r2, c2), steps in vis.items():
            if r2 == 1 and c2 not in targetC.values():
                yield r2, c2, steps

def s2g(state):
    return [list(row) for row in state.split('\n')]

def getNewStates(state):
    grid = state.split('\n')
    R, C = len(grid), len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] in 'ABCD':
                for rr, cc, steps in getMoves(grid, r, c, R, C):
                    g2 = s2g(state)
                    g2[r][c], g2[rr][cc] = g2[rr][cc], g2[r][c]
                    state2 = '\n'.join(''.join(row) for row in g2)
                    yield grid[r][c], state2, steps
from heapq import *
def dijk(S, T):
    dist = defaultdict(lambda: 10**10)
    pq = []
    def add(S, cost):
        if dist[S] <= cost: return
        dist[S] = cost
        heappush(pq, (cost, S))
    add(S, 0)
    while pq:

        c, U = heappop(pq)
        if dist[U] < c: continue
        if U == T: return c
        for thing, V, steps in getNewStates(U):
            w = COST[thing]
            add(V, c + w*steps)
    return None

    

def p1(v):
    lines = get_lines(v.replace(' ', '#'))
    C = len(lines[0])
    for i in range(len(lines)):
        if len(lines[i]) != C:
            lines[i] = lines[i] + '#'*(C - len(lines[i]))
    END = ['#############',
         '#...........#',
         '###A#B#C#D###',
         '###A#B#C#D###',
         '#############']

    S = '\n'.join(lines)
    T = '\n'.join(END)
    return dijk(S, T)

def p2(v):
    lines = get_lines(v.replace(' ', '#'))
    C = len(lines[0])
    for i in range(len(lines)):
        if len(lines[i]) != C:
            lines[i] = lines[i] + '#'*(C - len(lines[i]))

    lines.insert(3, '###D#B#A#C###')
    lines.insert(3, '###D#C#B#A###')
    S = lines
    T = ['#############',
         '#...........#',
         '###A#B#C#D###',
         '###A#B#C#D###',
         '###A#B#C#D###',
         '###A#B#C#D###',
         '#############']

    return dijk('\n'.join(S), '\n'.join(T))


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
