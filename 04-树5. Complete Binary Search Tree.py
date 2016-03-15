# coding: UTF-8

solution = '''完全二叉树，每一层节点应该是2**（n-1)
前n层节点和，为2**n - 1
给定多少个数后，排序就会得到有序数列
然后通过上述两个公式计算出最底层实际节点数
通过2**（n-1）计算出最底层应有节点数
然后计算出左右子树节点差
就能算出根节点，然后递归，每一层的节点就得以解决了'''

from math import log


def FindRoot(lst):
    num_element = len(lst)  # the number of elements
    num_full_level = int(log(num_element, 2))
    num_element_last = num_element - 2 ** (num_full_level) + 1
    half_last = 2 ** (num_full_level - 1)
    if half_last >= num_element_last:
        # all the last level element in the left
        left = num_element_last
        right = 0
    else:
        # some in the right, left is full
        left = half_last
        right = num_element_last - half_last
    lst.sort()
    lst_full = lst[left:len(lst) - right]
    res = lst_full[len(lst_full) / 2]
    index = lst.index(res)
    return res, index   # return the middle of the full tree


def Solve(lst):
    lst.sort()
    res = []
    queue = [lst]
    while len(queue) != 0:  # if there is small seq in
        # print 'queue is', queue
        temp = queue.pop(0)  # pop the first subseq

        if len(temp) == 1:
            # if there is only one element in the seq, put it in the res
            res.append(temp[0])
        else:
            # if not, find the root of the seq,
            # and sperate it into two piece,put in the back of queue
            root, index = getroot(temp)
            res.append(root)
            queue.append(temp[:index])
            if index != len(temp) - 1:  # if there is right seq
                queue.append(temp[index + 1:])
    return res


def getroot(lst):
    lst.sort()
    height = int(log(len(lst) + 1, 2))
    NumInLast = len(lst) - 2**height + 1
    NumOfLeft = 2**(height - 1) - 1 + min(NumInLast, 2**(height - 1))
    return lst[NumOfLeft], NumOfLeft



num = raw_input()
lst = raw_input().split()

for i in Solve(lst):
    print i,

a = 6
lst = [i for i in range(a)]
print Solve(lst)
print FindRoot(lst)
# print getroot(lst)
