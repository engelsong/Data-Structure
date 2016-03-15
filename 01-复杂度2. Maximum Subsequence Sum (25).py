

def MaxSubseqSum4(lst):

    maxsum = 0
    thissum = 0
    thisstart = 0
    start = 0
    stop = 0
    start_find = 0
    for i in lst:
        if not start_find:
            thisstart = i
            start_find = 1
        thissum += i
        if thissum > maxsum:
            maxsum = thissum
            start = thisstart
            stop = i
        if thissum < 0:
            thissum = 0
            start_find = 0

    return maxsum, start, stop


def outputFunc(lst):

    maxsum, start, stop = MaxSubseqSum4(lst)
    if maxsum <= 0 and 0 not in lst:
        maxsum = 0
        start = lst[0]
        stop = lst[-1]

    return maxsum, start, stop


# num = raw_input()
# lst = map(int,raw_input().split())


# for x in outputFunc(lst):
#     print x,
a = [1, 2, 3, -20, 1, 2, 3, 4, 0]
print MaxSubseqSum4(a)
print outputFunc(a)
