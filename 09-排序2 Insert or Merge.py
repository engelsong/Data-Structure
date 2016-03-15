
def getLen(Orilst, Sortedlst, N):
    index = 1
    while index < N:
        temp = Orilst[index]
        loc = index
        while loc > 0:
            if temp < Orilst[loc - 1]:
                Orilst[loc] = Orilst[loc - 1]
                loc -= 1
            else:
                break
        Orilst[loc] = temp
        if Orilst[0:index] != Sortedlst[0:index]:
            break
        index += 1
    return index

def check(Sortedlst, index, N):
    num = index
    res = False
    while index + num - 1 < N:
        for i in range(index, index + num - 1):
            if Sortedlst[i] > Sortedlst[i + 1]:
                res = True
                break
        if res == True:
            break
        else:
            index += num
    if res is False and index < N:
        for i in range(index, N - 1):
            if Sortedlst[i] > Sortedlst[i + 1]:
                res = True
                break
    return res

def merge(Sortedlst, num, N):
    res = [0 for i in range(N)]
    for 
    





Orilst = [3, 1, 2, 8, 7, 5, 9, 4, 6, 0]
lst = [1, 2, 3, 7, 8, 5, 9, 4, 6, 0]
lst1 = [1, 3, 2, 8, 5, 7, 4, 9, 0, 6]
print getLen(Orilst, lst, 10)
print check(lst, getLen(Orilst, lst, 10), 10)
print Orilst




