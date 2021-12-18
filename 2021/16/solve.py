#!/usr/bin/env python
# https://adventofcode.com/2021/day/16

class BitStream:
    total_version = 0

    def __init__(self, data):
        self.data = data

    def handle(self):
        BitStream.total_version += int(self.read(3), 2)
        tid = int(self.read(3), 2)

        if tid == 4:
            self.read_literal()
        else:
            if self.read(1) == "0":
                bs = BitStream(self.read(int(self.read(15), 2)))
                while True:
                    try:
                        bs.handle()
                    except Exception:
                        break
            else:
                for i in range(int(self.read(11), 2)):
                    self.handle()

    def read(self, pos):
        value = self.data[:pos]
        self.data = self.data[pos:]
        return value

    def read_literal(self):
        v, c = "", "1"
        while c == "1":
            c = self.read(1)
            v += self.read(4)
        return int(v, 2)


BitStream(bin(int("1"+open("input.txt").read().strip(), base=16))[3:]).handle()
print(f"part1: {BitStream.total_version}")
