#!/usr/bin/env python3

test = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

import re

def p1(f):
    schedule = {}

    line = f
    line.sort(key = lambda x : re.findall(r'\d+', x)[4])
    line.sort(key = lambda x : re.findall(r'\d+', x)[3])
    line.sort(key = lambda x : re.findall(r'\d+', x)[2])
    line.sort(key = lambda x : re.findall(r'\d+', x)[1])
    line.sort(key = lambda x : re.findall(r'\d+', x)[0])
    gid = -1
    start = -1
    for line in f:
        nums = re.findall(r'\d+', line)
        if len(nums) == 6:
            ## guard begins shift
            gid = nums[5]
            if schedule.get(gid) == None:
                schedule[gid] = {'mins' : [0] * 60}
        elif re.match('falls asleep'):
            start = "%d:%d" % (nums[3], nums[4])
        elif re.match('wakes up', line):

        print(nums)
    return 0

def main():
    assert p1(test.split('\n')) == 240
    f = open("input").readlines()
    print(p1(f))
    return 0

if __name__ == "__main__":
    main()
