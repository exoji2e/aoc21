#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 16
def get_year(): return 2021

def tobits(line):
    bits = []
    for ch in line:
        v = int(ch, 16)
        bs = bin(v)[2:]
        bs = '0'*(4 - len(bs)) + bs
        for b in bs:
            bits.append(b)
    return ''.join(bits)

def getVT(bits, i):
    return int(bits[i:i+3], 2), int(bits[i+3: i+6])

def read(bits, i, no):
    return int(bits[i: i+no], 2), i + no

def parsePacket(bits, i):
    v, i = read(bits, i, 3)
    t, i = read(bits, i, 3)
    totV = v
    value = 0
    if t == 4:
        labels = []
        while 1:
            x, i = int(bits[i]), i+1    
            lab, i = read(bits, i, 4)
            labels.append(lab)
            if x == 0: break
        vs = 0
        for lab in labels:
            vs = vs*16 + lab
        value = vs
    else:
        values = []
        I, i = read(bits, i, 1)
        if I == 0: 
            L = 15
            totL, i = read(bits, i, L)
            si = i
            while i < si + totL:
                vsum, v, i = parsePacket(bits, i)
                totV += vsum
                values.append(v)
        else: 
            L = 11 
            no, i = read(bits, i, L)
            for _ in range(no):
                vsum, v, i = parsePacket(bits, i)
                totV += vsum
                values.append(v)
        if t == 0:
            value = sum(values)
        elif t == 1:
            value = 1
            for v in values:
                value *= v
        elif t == 2:
            value = min(values)
        elif t == 3:
            value = max(values)
        elif t == 5:
            value = 1 if values[0] > values[1] else 0
        elif t == 6:
            value = 1 if values[0] < values[1] else 0
        elif t == 7:
            value = 1 if values[0] == values[1] else 0
    return totV, value, i



    


def p1(v):
    bits = tobits(v.strip())
    return parsePacket(bits, 0)[0]

def p2(v):
    bits = tobits(v.strip())
    return parsePacket(bits, 0)[1]


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
