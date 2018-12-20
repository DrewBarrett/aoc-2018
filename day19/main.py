#!/usr/bin/env python3

import copy

def p1(lines):
    lines = [l.strip() for l in lines]
    IP = int(lines[0].split(' ')[-1])
    instrs = lines[1:]
    print(instrs)
    REGS = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
    }
    while True:
        currRegs = copy.deepcopy(REGS)
        instr = instrs[currRegs[IP]]
        A, B, C = instr.split(' ')[1:]
        A = int(A)
        B = int(B)
        C = int(C)
        typ = list(instr.split(' ')[0])[-1]
        inst = "".join(list(instr.split(' ')[0])[:-1])
        val1 = currRegs[A] if A < len(currRegs) else -1
        val2 = currRegs[B] if typ == 'r' else B
        res = 0
        if inst == 'add':
            res = val1 + val2
        elif instr.split(' ')[0] == 'seti':
            res = A
        elif inst == 'set':
            # setr
            res = val1
        elif inst == 'mul':
            res = val1 * val2
        elif inst == 'eqr':
            res = 1 if val1 == val2 else 0
        elif inst == 'eqi':
            res = 1 if A == val2 else 0
        elif inst == 'gtr':
            res = 1 if val1 > val2 else 0
        elif inst == 'gti':
            res = 1 if A > val2 else 0
        else:
            print("UNKNOWN INST", inst)
            exit(-1)
        REGS[C] = res
        #print("ip=%d" % (currRegs[IP],), currRegs.values(), instr, typ, REGS.values())
        REGS[IP] = REGS[IP] + 1
        if REGS[IP] > len(instrs) - 1 or REGS[IP] < 0:
            break
    print(REGS.values())
    return 0
def p2(lines):
    return 0

def main():
    test = """#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5""".split('\n')
    print(p1(test))
    f = open('input').readlines()
    print(p1(f))
    p2(f)
    return 0

if __name__ == "__main__":
    main()
