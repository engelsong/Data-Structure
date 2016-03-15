def MaxSubseqSum4(lst):
    """sovle it online,get sum from left to right, if the sum below zero then abondon it"""
    #O(n)
    maxsum = 0
    thissum = 0
    length = len(lst)
    for i in range(length):
        thissum += lst[i]
        if thissum > maxsum:
            maxsum = thissum
        elif thissum < 0:
            thissum = 0

    return maxsum

firstline = raw_input()
lst = map(int, raw_input().split())
print MaxSubseqSum4(lst)
