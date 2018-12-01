#!/usr/bin/env python3

if __name__ == "__main__":
    f = open("input", 'r')
    s = 0
    ff = [0]
    re = 0
    p2 = True
    f = f.readlines()
    while p2:
        for l in f:
            s += int(l)
            if p2 == True:
                if (s in ff):
                    re = s
                    p2 = False
                ff.append(s)
        print("Part 1:", s)

    print("Part 2:", re)
