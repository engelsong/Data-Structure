firstline = raw_input().split()

start = firstline[0]
num = int(firstline[1])
K = int(firstline[2])
InPut = {}
for i in range(num):
    addr, data, nextone = raw_input().split()
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
