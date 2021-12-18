#!/usr/bin/env python
# https://adventofcode.com/2021/day/16

from math import prod
from operator import gt, lt, eq
f = [sum, prod, min, max, None, gt, lt, eq]


class BITS:
    total = 0

    def __init__(self,s):
        self.s = s
        self.off = 0

    def handle(self):
        BITS.total += int(self.read(3),2)
        print(BITS.total)
        type = int(self.read(3),2)
        if type==4: return self.get_literal()
        return f[type](self.get_res()) if type in range(5) else f[type](*self.get_res())

    def read(self, n):
        res = self.s[self.off:self.off+n]
        self.off += n
        return res

    def get_res(self):
        if self.read(1)=='0':
            res = []
            subp = BITS(self.read(int(self.read(15),2)))
            while subp.off<len(subp.s):
                res.append(subp.handle())
            return res
        else:
            return [self.handle() for c in range(int(self.read(11),2))]

    def get_literal(self):
        c,e = '','1'
        while e!='0':
            e = self.read(1)
            t = self.read(4)
            c += t
        return int(c,2)

aoc_input = open("input.txt").read().strip()
s = bin(int(aoc_input,16))[2:]
s = s.zfill(len(aoc_input)*4)
r = BITS(s).handle()
print('part1:',BITS.total)
print('part2:',r)
