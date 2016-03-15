def Multi(lst1, lst2):
    dict = {}
    res = []
    for i in range(len(lst1))[1::2]:
        for j in range(len(lst2))[1::2]:
            # print 'i, j = ', i, j
            co = lst1[i - 1] * lst2[j - 1]
            exp = lst1[i] + lst2[j]
            # print 'co, exp = ', co, exp
            if exp in dict:
                dict[exp] += co
            else:
                dict[exp] = co
    key = sorted(dict.keys(), reverse = True)
    for x in key:
        if dict[x] != 0:
            res.append(dict[x])
            res.append(x)
    return res


def Sum(lst1, lst2):
    res = []
    index1 = 1
    index2 = 1
    if len(lst1) == 0:
        res = lst2
    else:
        if len(lst2) == 0:
            res = lst1
        else:

            while 1:
                if lst1[index1] == lst2[index2]:
                    temp = lst1[index1 - 1] + lst2[index2 - 1]
                    if temp != 0:
                        res.append(temp)
                        res.append(lst1[index1])
                    index1 += 2
                    index2 += 2
                elif lst1[index1] > lst2[index2]:
                    res.append(lst1[index1 - 1])
                    res.append(lst1[index1])
                    index1 += 2
                else:  # lst1[index1] < lst2[index2]:
                    res.append(lst2[index2 - 1])
                    res.append(lst2[index2])
                    index2 += 2
                if index1 > len(lst1):
                    if index2 < len(lst2):
                        res += lst2[index2 - 1:]
                    break
                else:
                    if index2 > len(lst2):
                        res += lst1[index1 - 1:]
                        break
    return res

m2 = [0, 0]
m1 = [1,1,-1,0]
# print Sum(m1, m2)
# print Multi(m1, m2)
# m1 = map(int, raw_input().split())[1:]
# m2 = map(int, raw_input().split())[1:]
res1 = Multi(m1, m2)
res2 = Sum(m1, m2)
if len(res1) != 0:
    for i in res1:
        print i,
    print
else:
    print 0, 0
if len(res2) != 0:
     for j in res2:
        print j,
else:
    print 0, 0,