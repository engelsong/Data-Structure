import time
import random


a = []
n = 100
for x in range(n):
    a.append(random.randint(-10, 10))


def MaxSubseqSum1(lst):
    """ voilence way to slove this problem, check every possible subsequence"""
    # O(n^3)
    maxsum = 0
    length = len(lst)
    for i in range(length): #left side 
        for j in range(i + 1, length):#right side
            thissum = 0
            for k in range(i, j):#check the sum
                thissum += lst[k]
                if thissum > maxsum:
                    maxsum = thissum

    return maxsum


def MaxSubseqSum2(lst):
    """ a slight better way than 1, not plus the element repeatly"""
    # O(n^2)
    maxsum = 0
    length = len(lst)
    for i in range(length): #left side
        thissum = 0
        for j in range(i, length): #plus every element to right
            thissum += a[j]
            if thissum > maxsum:
                maxsum = thissum

    return maxsum


def MaxSubseqSum3(lst):
    """divide and solve, recursion way, check maxsum for left and right and cross the mid,
    the maxsum of those will be the slovsion"""
    # O(n * logn)
    length = len(lst)

    if length == 1: #basement of recursion, when the subseq only has one element, return it
        return lst[0]

    mid = length / 2 #find the mid of list, and split in two from the mid
    left = lst[:mid]
    right = lst[mid:]

    max_left = MaxSubseqSum3(left) #get the left side maxsum
    max_right = MaxSubseqSum3(right)#get the right side maxsum
    if max_left < max_right: #get the bigger one
        max = max_right
    else:
        max = max_left

    temp_sum = 0 # get the maxsum from mid to left
    left_sum = lst[mid - 1]
    for i in range(mid)[::-1]:
        temp_sum = temp_sum + lst[i]
        if left_sum < temp_sum:
            left_sum = temp_sum

    temp_sum = 0 # get the maxsum from mid to right
    right_sum = lst[mid]
    for j in range(mid, length):
        temp_sum = temp_sum + lst[j]
        if right_sum < temp_sum:
            right_sum = temp_sum

    mid_sum = left_sum + right_sum # get the maxsum cross the mid 

    if max < mid_sum:
        max = mid_sum

    return max


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


start1 = time.time()
sum1 =  MaxSubseqSum1(a)
stop1 = time.time()


start2 = time.time()
sum2 =  MaxSubseqSum2(a)
stop2 = time.time()


start3 = time.time()
sum3 =  MaxSubseqSum3(a)
stop3 = time.time()


start4 = time.time()
sum4 =  MaxSubseqSum4(a)
stop4 = time.time()


cost1 = (stop1 - start1)
cost2 = (stop2 - start2)
cost3 = (stop3 - start3)
cost4 = (stop4 - start4)


print sum1
print 'sum1 cost: ', cost1

print sum2
print 'sum2 cost: ', cost2

print sum3
print 'sum3 cost: ', cost3

print sum4
print 'sum4 cost: ', cost4


