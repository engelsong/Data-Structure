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
        self.path = []
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
        return res

    def jump(self, loc):
        # print 'path is ',self.path
        # print' loc is ', loc
        firstloc = self.firstJump()
        self.path.append(loc)
        if self.lake.getBankDis(loc) <= self.maxDis:
            res = True
        else:
            for croc in self.getNext(loc):
                # print 'croc is ', croc
                if croc not in self.path and croc not in firstloc:
                    res = self.jump(croc)
                    if res == True:
                        break
            else:
                res = False
        return res

    def getOut(self):
        res = False
        firstloc = self.firstJump()
        for v in firstloc:
            if self.jump(v) is True:
                res = True
                break
        return res


crocNum, maxDis = map(int,raw_input().split())


theLake = lake()
the007 = person(maxDis, theLake)
for i in range(crocNum):
    c1, c2 = map(int,raw_input().split())
    theLake.addCroc(c1, c2)

if the007.getOut():
    print 'Yes'
else:
    print 'No'

