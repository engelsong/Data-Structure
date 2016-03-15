# coding: UTF-8
import random
import time


def Bubble_Sort(lst):
    lenth = len(lst)
    for j in range(lenth - 1):
        is_changed = 0
        for i in range(lenth - j - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                is_changed = 1
        if is_changed == 0:
            break
    return lst


def Insertion_Sort(lst):
    lenth = len(lst)
    for i in range(1, lenth):
        temp = lst[i]
        loc = i
        while loc > 0:
            if temp < lst[loc - 1]:
                lst[loc] = lst[loc - 1]
                loc -= 1
            else:
                break
        lst[loc] = temp
    return lst


def Shell_Sort_Sedgewick(lst):
    lenth = len(lst)
    sedgewick = [109, 41, 19, 5, 1]
    for x in sedgewick:
        for i in range(x, lenth):
            temp = lst[i]
            loc = i
            while loc > 0:
                if temp < lst[loc - x]:
                    lst[loc] = lst[loc - x]
                    loc -= x
                else:
                    break
            lst[loc] = temp
    return lst


def percdown(lst, p, lenth):
    parent = p
    child = parent * 2 + 1
    while child <= lenth - 1:
        if child != lenth - 1:
            if lst[child] < lst[child + 1]:
                # find the bigger one in left and right child
                child += 1
        if lst[parent] > lst[child]:
            break
        else:
            temp = lst[child]
            lst[child] = lst[parent]
            lst[parent] = temp
            parent = child
            child = parent * 2 + 1


def Heap_Sort(lst):
    lenth = len(lst)
    index = lenth / 2 - 1
    while index >= 0:
        percdown(lst, index, lenth)
        index -= 1
    index = lenth - 1
    while index > 0:
        lst[0], lst[index] = lst[index], lst[0]
        percdown(lst, 0, index)
        index -= 1
    return lst


def merge(lst, templst, L, R, RightEnd):
    LeftEnd = R - 1
    tmp = L
    lenth = RightEnd - L + 1
    while L <= LeftEnd and R <= RightEnd:
        if lst[L] <= lst[R]:
            templst[tmp] = lst[L]
            L += 1
        else:
            templst[tmp] = lst[R]
            R += 1
        tmp += 1
    if L <= LeftEnd:
        for i in lst[L:LeftEnd + 1]:
            templst[tmp] = i
            tmp += 1
    if R <= RightEnd:
        for i in lst[R:RightEnd + 1]:
            templst[tmp] = i
            tmp += 1
    lst[RightEnd + 1 - lenth:RightEnd +
        1] = templst[RightEnd + 1 - lenth:RightEnd + 1]


def MSort(lst, templst, L, RightEnd):
    if L < RightEnd:
        center = (L + RightEnd) / 2
        MSort(lst, templst, L, center)
        MSort(lst, templst, center + 1, RightEnd)
        merge(lst, templst, L, center + 1, RightEnd)


def Merge_Sort(lst):
    templst = [0 for i in range(len(lst))]
    lenth = len(lst)
    MSort(lst, templst, 0, lenth - 1)
    return lst


def xmerge(lst, templst, L, R, RightEnd):
    LeftEnd = R - 1
    tmp = L
    lenth = RightEnd - L + 1
    while L <= LeftEnd and R <= RightEnd:
        if lst[L] <= lst[R]:
            templst[tmp] = lst[L]
            L += 1
        else:
            templst[tmp] = lst[R]
            R += 1
        tmp += 1
    if L <= LeftEnd:
        for i in lst[L:LeftEnd + 1]:
            templst[tmp] = i
            tmp += 1
    if R <= RightEnd:
        for i in lst[R:RightEnd + 1]:
            templst[tmp] = i
            tmp += 1


def merge_pass(lst, templst, sublen):
    lenth = len(lst)
    index = 0
    while index <= lenth - sublen * 2:
        xmerge(lst, templst, index, index + sublen, index + sublen * 2 - 1)
        index += sublen * 2
    if index + sublen < lenth:
        xmerge(lst, templst, index, index + sublen, lenth - 1)
    else:
        templst[index:lenth + 1] = lst[index:lenth + 1]


def Merge_Sort_InR(lst):
    lenth = len(lst)
    templst = [0 for i in range(lenth)]
    sublen = 1
    while sublen < lenth:
        merge_pass(lst, templst, sublen)
        sublen *= 2
        merge_pass(templst, lst, sublen)
        sublen *= 2
    return lst


def median3(lst, left, right):
    center = (left + right) / 2
    if lst[left] > lst[center]:
        lst[left], lst[center] = lst[center], lst[left]
    if lst[left] > lst[right]:
        lst[right], lst[left] = lst[left], lst[right]
    if lst[center] > lst[right]:
        lst[center], lst[right] = lst[right], lst[center]
    lst[center], lst[right - 1] = lst[right - 1], lst[center]
    return lst[right - 1]


def quicksort(lst, left, right):
    if right - left > 10:
        pivot = median3(lst, left, right)
        i = left + 1
        j = right - 2
        while 1:
            while lst[i] < pivot:
                i += 1
            while lst[j] > pivot:
                j -= 1
            if i < j:
                lst[i], lst[j] = lst[j], lst[i]
            else:
                break
        lst[i], lst[right - 1] = lst[right - 1], lst[i]
        quicksort(lst, left, i - 1)
        quicksort(lst, i + 1, right)
    else:
        lenth = right - left + 1
        for i in range(left + 1, right + 1):
            temp = lst[i]
            loc = i
            while loc > left:
                if temp < lst[loc - 1]:
                    lst[loc] = lst[loc - 1]
                    loc -= 1
                else:
                    break
            lst[loc] = temp
    return lst


def Quick_Sort(lst):
    quicksort(lst, 0, len(lst) - 1)
    return lst


def Table_Sort(lst):
    lenth = len(lst)
    table = [i for i in range(lenth)]
    for i in range(1, lenth):
        temp = lst[table[i]]
        loc = i
        while loc > 0:
            if temp < lst[table[loc - 1]]:
                table[loc] = table[loc - 1]
                loc -= 1
            else:
                break
        table[loc] = i
    return table


def check(name):
    global num
    global lst
    templst = lst[:]
    start = time.time()
    name(templst)
    stop = time.time()
    print templst == range(num)
    print stop - start


num = 100000
lst = range(num)
random.shuffle(lst)

# print lst

# N = int(raw_input())
# a = map(int, raw_input().split())
# for i in Insertion_Sort(lst):
#     print i,


# check(Bubble_Sort)
# check(Insertion_Sort)
# check(Shell_Sort_Sedgewick)
# check(Heap_Sort)
# check(Merge_Sort)
# check(Merge_Sort_InR)
check(Quick_Sort)
