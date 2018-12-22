#!/usr/bin/env python3

def p1(lines):
    c = 0
    board = {}
    claims = []
    for line in lines:
        line = line.split(' ')
        claim = line[0][1:]
        offsets = line[2][:-1].split(',')
        size = line[3].split('x')
        claims.append(claim)
        for i in range(int(size[0])):
            for j in range(int(size[1])):
                if board.get(i + int(offsets[0])) == None:
                    board[i + int(offsets[0])] = {}
                    board[i + int(offsets[0])][j + int(offsets[1])] = {'claims': 1, 'owner': claim}
                else:
                    if board.get(i + int(offsets[0])).get(j + int(offsets[1])) == None:
                        board[i + int(offsets[0])][j + int(offsets[1])] = {'claims': 1, 'owner': claim}
                    else:
                        board[i + int(offsets[0])][j + int(offsets[1])]['claims'] += 1
                        #if board[i + int(offsets[0])][j + int(offsets[1])]['owner'] is not claim:
                        try:
                            #print('removing', (board[i + int(offsets[0])][j + int(offsets[1])]['owner']))
                            claims.remove(board[i + int(offsets[0])][j + int(offsets[1])]['owner'])
                        except:
                            #print('failed')
                            pass
                        try:
                            claims.remove(claim)
                        except:
                            pass
                        board[i + int(offsets[0])][j + int(offsets[1])]['owner'] = claim
        #print(board, claims)
    for i in board.keys():
        string = ""
        for j in board[i].keys():
            if board[i][j]['claims'] >= 2:
                string += 'X'
                c += 1
            elif board[i][j]['claims'] == 0:
                print("")
            elif board[i][j]['claims'] == 1:
                string += board[i][j]['owner']
        #print(string)
    #print(claims)
    return c, int(claims[0])
def p2(lines):
    return 0

def main():
    assert p1(['#1 @ 1,3: 4x4',
               '#2 @ 3,1: 4x4',
               '#3 @ 5,5: 2x2']) == (4, 3)
    f = open('input').readlines()
    print(p1(f))
    p2(f)
    return 0

if __name__ == "__main__":
    main()
