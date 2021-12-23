#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *

from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 22
def get_year(): return 2021

def parse(line):
    line = line.replace('x=', '').replace(',', ' ').replace('..', ' ').replace('y=', '').replace('z=', '')
    return lazy_ints(line.split())

def inside(corner, cube):
    x, y, z = corner
    xx, xx2, yy, yy2, zz, zz2 = cube
    return xx <= x <= xx2 and yy <= y <= yy2 and zz <= z <= zz2

def common(xs1, xs2):
    x10, x11 = xs1
    x20, x21 = xs2
    l = max(x10, x20)
    r = min(x11, x21)
    return l, r
def hasCommon(xs1, xs2):
    l, r = common(xs1, xs2)
    return l <= r

def overlap(sq1, sq2):
    x1, x2, y1, y2, z1, z2 = sq1
    xx1, xx2, yy1, yy2, zz1, zz2 = sq2
    return hasCommon((x1,x2), (xx1, xx2)) and hasCommon((y1,y2), (yy1, yy2)) and hasCommon((z1,z2), (zz1, zz2))

def intersect(sq1, sq2):
    x1, x2, y1, y2, z1, z2 = sq1
    xx1, xx2, yy1, yy2, zz1, zz2 = sq2
    xl, xr = common((x1,x2), (xx1, xx2)) 
    yl, yr = common((y1,y2), (yy1, yy2))
    zl, zr = common((z1,z2), (zz1, zz2))
    return xl, xr, yl, yr, zl, zr

def on(x, x2, y, y2, z, z2, cubes):
    over = 0
    for cube in cubes:
        cmd, xx, xx2, yy, yy2, zz, zz2 = cube
        if overlap((x, x2, y, y2, z, z2),(xx, xx2, yy, yy2, zz, zz2)):
            over += 1
    cubes.append(('on', x, x2, y, y2, z, z2))

def bounds(x0, xl, xr, x1):
    bnds = []
    for l, r in [(x0, xl-1), (xl, xr), (xr+1, x1)]:
        if l <= r: bnds.append((l, r))
    return bnds

def split(cube1, torem):
    x0, x1, y0, y1, z0, z1 = cube1
    xl, xr, yl, yr, zl, zr = torem
    boxes = []
    for x2, x3 in bounds(x0, xl, xr, x1):
        for y2, y3 in bounds(y0, yl, yr, y1):
            for z2,z3 in bounds(z0, zl, zr, z1):
                boxes.append((x2, x3, y2, y3, z2, z3))
    boxes.remove(torem)
    return boxes


def onoff(cmd, c0, cubes):
    othercubes = []
    for cmd2, cube in cubes:
        if overlap(c0,cube):
            intersecting_box = intersect(c0,cube)
            othersmaller = split(cube, intersecting_box)
            for sm in othersmaller:
                othercubes.append((cmd2, sm))
        else:
            othercubes.append((cmd2, cube))
    othercubes.append((cmd, c0))
    return othercubes


def p1(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    lights = {}
    for i, ins in enumerate(data):
        db(f'{i}/{len(data)}')
        cmd, x1, x2, y1, y2, z1, z2 = ins
        for x in range(max(x1, -50), min(x2, 50) + 1):
            for y in range(max(y1, -50), min(y2, 50) + 1):
                for z in range(max(z1, -50), min(z2, 50) + 1):
                    if cmd == 'on':
                        lights[x,y,z] = 1
                    else:
                        lights[x,y,z] = 0

    return sum(lights.values())

def p2(v):
    lines = v.strip().split('\n')
    data = [parse(line) for line in lines]
    su = 0
    cubes = []
    for i, ins in enumerate(data):
        cmd, x, x2, y, y2, z, z2 = ins
        cubes = onoff(cmd, (x, x2, y, y2, z, z2), cubes)
    tot = 0
    for cmd, cube in cubes:
        if cmd == 'on':
            xl, xr, yl, yr, zl, zr = cube
            sz = (xr - xl + 1)*(yr - yl + 1) * (zr - zl + 1)
            tot += sz     
    return tot

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
