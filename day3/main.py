#!/usr/bin/env python3

def p1(lines):
    c = 0
    board = {} # TODO: Add ownership table
    for line in lines:
        line = line.split(' ')
        offsets = line[2][:-1].split(',')
        size = line[3].split('x')
        for i in range(int(size[0])):
            for j in range(int(size[1])):
                if board.get(i + int(offsets[0])) == None:
                    board[i + int(offsets[0])] = {}
                    board[i + int(offsets[0])][j + int(offsets[1])] = 1
                else:
                    if board.get(i + int(offsets[0])).get(j + int(offsets[1])) == None:
                        board[i + int(offsets[0])][j + int(offsets[1])] = 1
                    else:
                        board[i + int(offsets[0])][j + int(offsets[1])] += 1
    for i in board.keys():
        for j in board[i].keys():
            if board[i][j] >= 2:
                c += 1
            if board[i][j] == 0:
                print("")
    print(c)
    return c
def p2(lines):
    return 0

def main():
    assert p1(['#1 @ 1,3: 4x4',
               '#2 @ 3,1: 4x4',
               '#3 @ 5,5: 2x2']) == 4
    f = open('input').readlines()
    p1(f)
    p2(f)
    return 0

if __name__ == "__main__":
    main()
