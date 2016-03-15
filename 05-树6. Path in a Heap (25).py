class MinHeap(object):

    """return the smallest one of the heap"""

    def __init__(self, MinData=-10e10):
        self.Size = 0
        self.Data = [MinData]
        self.MinData = MinData

    def Insert(self, item):
        if item < self.MinData:
            raise IOError("Out of the heap's range")
        self.Size += 1
        pos = self.Size
        self.Data.append(item)
        while self.Data[pos / 2] > item:
            self.Data[pos] = self.Data[pos / 2]
            pos /= 2
        self.Data[pos] = item

    def FindPath(self, index):
        res = []
        while index >= 1:
            res.append(self.Data[index])
            index /= 2
        return res

useless = raw_input()
lst = map(int,raw_input().split())
indexs = map(int, raw_input().split())

# usrin = '46 23 26 24 10'
# lst = usrin.split()
# indexs = '5 4 3'.split()


myheap2 = MinHeap()
for x in lst:
    myheap2.Insert(x)



for i in indexs:
    for j in myheap2.FindPath(int(i)):
        print j,
    print
