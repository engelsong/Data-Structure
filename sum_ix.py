import time


def sum1(x, n):
    res = 0
    for i in range(1, n + 1):
        res += (i * (x ** i))
    return res


def sum2(x, n):
    res = n
    for i in range(n - 1, 0, -1):
        res = i + x * res
    return res*x

n = 10000


start1 = time.time()
for i in xrange(n):
    sum1(3.14, 10)
stop1 = time.time()


start2 = time.time()
for i in xrange(n):
    sum2(3.14, 10)
stop2 = time.time()


sum1_cost = (stop1 - start1) / n
sum2_cost = (stop2 - start2) / n

print sum1(3.14, 10)
print 'sum1 cost: ', sum1_cost
print sum2(3.14, 10)
print 'sum2 cost: ', sum2_cost
