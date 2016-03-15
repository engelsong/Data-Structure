from math import log


def getroot(num):
    height = int(log(num + 1, 2))
    NumInLast = num - 2 ** height + 1
    NumOfLeft = 2 ** (height - 1) - 1 + min(NumInLast, 2 ** (height - 1))
    return NumOfLeft


Num = int(raw_input())
lst = map(int, raw_input().split())
lst.sort()
res = [None for i in range(Num)]


def solve(left, right, root):
    global lst
    global res
    lenth = right - left + 1
    if lenth == 0:
        return
    NumLeft = getroot(lenth)
    res[root] = lst[left + NumLeft]
    LeftRoot = root * 2 + 1
    RightRoot = LeftRoot + 1
    solve(left, left + NumLeft - 1, LeftRoot)
    solve(left + NumLeft + 1, right, RightRoot)

solve(0, Num - 1, 0)
for i in res:
    print i,
