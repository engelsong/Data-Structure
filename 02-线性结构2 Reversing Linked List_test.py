firstline = '00100 6 2'.split()
userin = """00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218""".split('\n')

start = firstline[0]
num = int(firstline[1])
K = int(firstline[2])
InPut = {}
for i in userin:
    addr, data, nextone = i.split()
    InPut[addr] = [data, nextone]

stack = []
keyword = start
res = []

for t in range(len(InPut)):
    for k in xrange(K):
        stack.append(keyword)
        keyword = InPut[keyword][1]
        if keyword == '-1':
            break
    else:
        res += stack[::-1]
        stack = []
    if keyword == '-1':
        if len(stack) < K:
            res += stack
        else:
            res += stack[::-1]
        break

time = len(res)
for x in xrange(time - 1):
    print '{} {} {}'.format(res[x], InPut[res[x]][0], res[x + 1])
print '{} {} {}'.format(res[-1], InPut[res[-1]][0], '-1')