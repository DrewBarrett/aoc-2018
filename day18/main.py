#!/usr/bin/env python3

import copy
import functools

@functools.lru_cache(maxsize=128)
def checkAdjacent(y, x, state):
    origx = x
    origy = y
    dic = {'#': 0,
           '|': 0,
           '.': 0}
    ys = [y - 1, y, y + 1]
    xs = [x - 1, x, x + 1]
    for y in ys:
        if y > len(state) - 1 or y < 0:
            continue
        for x in xs:
            if x > len(state[y]) - 1 or x < 0 or (x == origx and y == origy):
                continue
            x = state[y][x]
            if x not in dic:
                continue
            dic[x] = dic[x] + 1

    return dic

def p1(lines, r):
    currentState = copy.deepcopy(lines)
    for l in currentState:
        l = l.strip()
    nextState = copy.deepcopy(currentState)
    for i in range(r):
        currentState = copy.deepcopy(nextState)
        nextState = copy.deepcopy(currentState)
        # look at current state, modify next
        for l in range(len(currentState)):
            string = ""
            currentState[l] = list(currentState[l])
            nextState[l] = list(nextState[l])
            for let in range(len(currentState[l])):
                string += currentState[l][let]
                fuck = [tuple(x) for x in currentState]
                adjacent = checkAdjacent(l, let, tuple(fuck))
                if currentState[l][let] == '.':
                    if adjacent['|'] >= 3:
                        nextState[l][let] = '|'
                elif currentState[l][let] == '|':
                    if adjacent['#'] >= 3:
                        nextState[l][let] = '#'
                elif currentState[l][let] == '#':
                    if adjacent['#'] < 1 or adjacent['|'] < 1:
                        nextState[l][let] = '.'
            #print(string)
        #print(i)
    # calculate final value
    trees = 0
    yards = 0
    for i in nextState:
        for j in i:
            if j == '|':
                trees += 1
            elif j == '#':
                yards += 1
    return trees * yards
def p2(lines):
    return 0

def main():
    test = """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.""".split('\n')
    assert p1(test, 10) == 1147
    f = open('input').readlines()
    print(p1(f, 10), p1(f, 1000000000))
    p2(f)
    return 0

if __name__ == "__main__":
    main()
