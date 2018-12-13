#!/usr/bin/env python3

def p1(lines):
    carts = []
    y = 0
    for line in lines:
        x = 0
        if line[-1] == '\n':
            line = line[:-1]
        for char in line:
            if char in ['^', '>', '<', 'v']:
                carts.append([x, y, char, 0])
            line = line.replace('^', '|')
            line = line.replace('>', '-')
            line = line.replace('<', '-')
            line = line.replace('v', '|')
            x += 1
        print(line)
        y += 1
    while True:
        carts.sort(key=lambda cart: cart[0])
        carts.sort(key=lambda cart: cart[1])
        for cart in carts:
            if cart[2] == '^':
                cart[1] -= 1
            elif cart[2] == '>':
                cart[0] += 1
            elif cart[2] == '<':
                cart[0] -= 1
            elif cart[2] == 'v':
                cart[1] += 1
            if lines[cart[1]][cart[0]] == '\\':
                if cart[2] == '^':
                    cart[2] = '<'
                elif cart[2] == '>':
                    cart[2] = 'v'
                elif cart[2] == '<':
                    cart[2] = '^'
                elif cart[2] == 'v':
                    cart[2] = '>'
            elif lines[cart[1]][cart[0]] == '/':
                if cart[2] == '^':
                    cart[2] = '>'
                elif cart[2] == '<':
                    cart[2] = 'v'
                elif cart[2] == '>':
                    cart[2] = '^'
                elif cart[2] == 'v':
                    cart[2] = '<'
            elif lines[cart[1]][cart[0]] == '+':
                if cart[3] == 0:
                    if cart[2] == '^':
                        cart[2] = '<'
                    elif cart[2] == '<':
                        cart[2] = 'v'
                    elif cart[2] == '>':
                        cart[2] = '^'
                    elif cart[2] == 'v':
                        cart[2] = '>'
                    # turnleft
                elif cart[3] == 1:
                    # go straight
                    pass
                elif cart[3] == 2:
                    # go right
                    if cart[2] == '^':
                        cart[2] = '>'
                    elif cart[2] == '<':
                        cart[2] = '^'
                    elif cart[2] == '>':
                        cart[2] = 'v'
                    elif cart[2] == 'v':
                        cart[2] = '<'
                    cart[3] = -1
                cart[3] += 1
            i = 0
            remov = []
            index = 0
            for c in carts:
                if c[0] == cart[0] and c[1] == cart[1]:
                    remov.append(index)
                    i += 1
                index += 1
            if i > 1:
                remov.sort(reverse=True)
                for cc in remov:
                    print('Removing %d' % (cc,))
                    carts.pop(cc)
                print([cart[0], cart[1]])
        if len(carts) <= 1:
            return carts

    #return [3, 7]
def p2(lines):
    return 0

def main():
    print(p1(['/->-\       ',\
        '|   |  /----\\',\
        '| /-+--+-\  |',\
        '| | |  | v  |',\
        '\-+-/  \-+--/',\
        '  \------/   ']))
    print(p1(['/>-<\  ',
              '|   |  ',
              '| /<+-\\',
              '| | | v',
              '\\>+</ |',
              '  |   ^',
              '  \\<->/']))
    f = open('input').readlines()
    print(p1(f))
    p2(f)
    return 0

if __name__ == "__main__":
    main()
