

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

key = [0 for i in range(51)]
num = int(raw_input())
data = map(int, raw_input().split())
for j in data:
    key[j] += 1
for i in range(51):
    if key[i] > 0:
        print '{}:{}'.format(i, key[i])
