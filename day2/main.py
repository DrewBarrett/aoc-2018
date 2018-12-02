#!/usr/bin/env python3


def p1(inp):
    two = 0
    three = 0
    for c in range(len(inp)):
        i = inp[c]
        cur = {}
        for j in i:
            if cur.get(j) != None:
                cur[j] += 1
            else:
                cur[j] = 1
        for j in cur.values():
            if j == 2:
                two += 1
                break
        for j in cur.values():
            if j == 3:
                three += 1
                break
    return two * three

def p2(one, two, debug=None):
    diff = 0
    for i in range(len(one)):
        if (one[i] != two[i]):
            diff += 1
    if diff == 1:
        if not debug:
            print(one, two)
        return 1
    return 0


def main():
    f = open('input').readlines()
    assert p1(['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']) == 12
    print(p1(f))
    assert p2('fghij', 'fguij', 1) == 1
    for i in f: # O(n^2)
        for j in f:
            p2(i, j)

if __name__ == "__main__":
    main()
