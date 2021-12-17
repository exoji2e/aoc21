#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 17
def get_year(): return 2021

def solve(v):
    _, _, x, y = v.split()
    def getLs(s):
        s = s.replace('.', ' ').replace('=', ' ').replace(',', '')
        lis = lazy_ints(s.split())
        return lis[-2], lis[-1]
    xL = getLs(x)
    yL = getLs(y)
    def inT(x, y):
        return xL[0] <= x <= xL[1] and yL[0] <= y <= yL[1]
    def test(dx, dy):
        x, y = 0, 0
        Ly = 0
        ok = False
        while x <= 67 and y >= -215: 
            x, y = x + dx, y + dy
            dx = max(0, dx - 1)
            dy -= 1
            Ly = max(Ly, y)
            ok = ok or inT(x, y)
        return ok, Ly
    maxX = max(xL)
    assert min(xL) > 0, f"Doesn't work for negative x target:{xL}"
    mY = 0
    cnt = 0
    for dx in range(1, maxX+1):
        for dy in range(min(yL), 2000):
            ok, ly = test(dx, dy)
            if ok:
                cnt += 1
                mY = max(mY, ly)
    return mY, cnt

def p1(v):
    return solve(v)[0]

def p2(v):
    return solve(v)[1]


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
