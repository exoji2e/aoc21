#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import run, run_samples, get_commands
from utils import *
def get_day(): return 10
def get_year(): return 2021

match = {
    ')' : '(',
    '}' : '{',
    ']' : '[',
    '>' : '<',
}
p1sc = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
}
p2sc = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4
}

def extract(lines):
    incompl = []
    fail_sc = 0
    for line in lines:
        stack = []
        fail = False
        for ch in line:
            if ch in '[{(<':
                stack.append(ch)
            else:
                if stack[-1] != match[ch]:
                    fail_sc += p1sc[ch]
                    fail = True
                    break
                stack.pop()
        if not fail:
            incompl.append(stack)
    return fail_sc, incompl


def p1(v):
    lines = get_lines(v)
    return extract(lines)[0]

def p2(v):
    lines = get_lines(v)
    incompl = extract(lines)[1]
    scores = []
    for stack in incompl:
        tot = 0
        for ch in stack[::-1]:
            tot *= 5
            tot += p2sc[ch]
        scores.append(tot)
    scores.sort()
    return scores[len(scores)//2]


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
