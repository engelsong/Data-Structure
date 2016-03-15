def check(M, N, lst):
    res = True
    last = lst[0]
    seq = [i for i in range(last + 1, N + 1)]
    stack = [i for i in range(1, last)]
    if last > M:
        res = False
    else:
        for temp in lst[1:]:
            if temp > last:
                for x in range(last + 1, temp + 1):
                    if x in seq:
                        stack.append(x)
                        seq.remove(x)
                if len(stack) > M:
                    res = False
                    break
                else:
                    stack.pop(-1)
            elif temp < last:
                if temp != stack.pop(-1):
                    res = False
                    break
            last = temp

    return res

# M = 5
# N = 7
# lst = [1, 2, 3, 4, 5, 6, 7]
# print check(M, N, lst)
M, N, times = map(int, raw_input().split())
for t in range(times):
    lst = map(int, raw_input().split())
    if check(M, N, lst):
        print 'YES'
    else:
        print 'NO'