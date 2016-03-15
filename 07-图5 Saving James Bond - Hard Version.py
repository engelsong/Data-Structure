class lake(object):

    def __init__(self):
        self.crocs = []
        self.bank = 50.0
        self.island = 7.5

    def addCroc(self, x, y):
        self.crocs.append((x, y))

    def getDis(self, c1, c2):
        def getlens(a, b):
            res = None
            if (a < 0 and b < 0) or (a > 0 and b > 0):
                res = abs(a - b)
            else:
                res = abs(a) + abs(b)
            return res

        x = getlens(c1[0], c2[0])
        y = getlens(c1[1], c2[1])

        return (x ** 2 + y ** 2) ** 0.5

    def getBankDis(self, croc):
        res = self.bank - max(abs(croc[0]), abs(croc[1]))
        return res


class person(object):

    def __init__(self, maxDis, lake):
        self.lake = lake
        self.maxDis = maxDis
        self.path = {}
        self.dist = {}
        self.exit = []
        self.firstloc = self.firstJump()

    def getNext(self, loc):
        res = []
        for croc in self.lake.crocs:
            if croc != loc and self.lake.getDis(loc, croc) <= self.maxDis:
                res.append(croc)
        return res

    def firstJump(self):
        res = []
        for croc in self.lake.crocs:
            if self.lake.getDis((0, 0), croc) <= (self.maxDis + self.lake.island):
                res.append(croc)
                self.path[croc] = None
                self.dist[croc] = 1
        return res

    def jump(self, loc):
        res = False
        queue = [loc]
        while len(queue) != 0:
            temp = queue.pop(0)
            for croc in self.getNext(temp):
                if croc not in self.dist:
                    self.dist[croc] = self.dist[temp] + 1
                    self.path[croc] = temp
                    if self.lake.getBankDis(croc) <= self.maxDis:
                        res = True
                        self.exit.append(croc)
                    queue.append(croc)
        return res

    def getOut(self):
        res = False
        firstloc = self.firstJump()
        for v in firstloc:
            if self.jump(v) is True:
                res = True
                break
        return res

    def showShortestPath(self):
        outNum = 0
        outPath = []
        self.getOut()
        def cmpare(x, y):
            if self.dist[x] > self.dist[y]:
                return 1
            elif self.dist[x] < self.dist[y]:
                return -1
            else:
                return 0
        self.exit.sort(cmpare)
        temp = self.exit[0]
        outNum = self.dist[temp] + 1
        while temp is not None:
            outPath.insert(0, temp)
            temp = self.path[temp]
        return outNum, outPath



crocNum, maxDis = map(int,raw_input().split())


theLake = lake()
the007 = person(maxDis, theLake)
for i in range(crocNum):
    c1, c2 = map(int,raw_input().split())
    theLake.addCroc(c1, c2)

if not the007.getOut():
    print 0
else:
    lst = the007.showShortestPath()
    print lst[0]
    for i in lst[1]:
        print '{} {}'.format(i[0], i[1])


