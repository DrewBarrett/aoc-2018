#!/usr/bin/env python3

if __name__ == "__main__":
    f = open("input", 'r')
    s = 0
    for l in f:
        s += int(l)
    print(s)
