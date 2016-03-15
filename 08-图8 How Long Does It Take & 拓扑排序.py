class DAG(object):
    """docstring for DAG"""
    def __init__(self, MaxPoint = 1):
        self.MaxPoint = MaxPoint
        self.InDegree = [0 for i in range(MaxPoint)]
        self.InPoint = [[] for i in range(MaxPoint)]
        self.Point = [i for i in range(MaxPoint)] 
        self.Activity = [[-1 for i in range(MaxPoint)]
                     for i in range(MaxPoint)]
        self.EarstTime = {}
        self.TopSort = []

    def addOneAct(self, p1, p2, last=1):
        self.Activity[p1][p2] = last
        self.InDegree[p2] += 1
        self.InPoint[p2].append(p1)

    def calTime(self, point):
        '''CAREFUL'''
        LastingTime = 0
        for i in self.InPoint[point]:
            temp = self.EarstTime[i] + self.Activity[i][point]
            if temp > LastingTime:
                LastingTime = temp
        return LastingTime

    def connectedPoint(self, Point):
        res = []
        for v in range(len(self.Point)):
            if self.Activity[Point][v] != -1:
                res.append(v)
        return res
    
    def TopSorting(self):
        InDegree = self.InDegree
        res = True
        queue = []
        for p in self.Point:
            if InDegree[p] == 0:
                queue.append(p)
                self.EarstTime[p] = 0
        while len(queue) != 0:
            p = queue.pop(0)
            # print p
            self.TopSort.append(p)
            # if p not in self.EarstTime:
            self.EarstTime[p] = self.calTime(p)
            for q in self.connectedPoint(p):
                InDegree[q] -= 1
                if InDegree[q] == 0:
                    queue.append(q)
        if len(self.TopSort) != self.MaxPoint:
            res = False
        return res

# myproject = DAG(9)
# myproject.addOneAct(0, 1, 6)
# myproject.addOneAct(0, 2, 4)
# myproject.addOneAct(0, 3, 5)
# myproject.addOneAct(1, 4, 1)
# myproject.addOneAct(2, 4, 1)
# myproject.addOneAct(3, 5, 2)
# myproject.addOneAct(5, 4, 0)
# myproject.addOneAct(4, 6, 9)
# myproject.addOneAct(4, 7, 7)
# myproject.addOneAct(5, 7, 4)
# myproject.addOneAct(6, 8, 2)
# myproject.addOneAct(7, 8, 4)

# myproject = DAG(4)
# myproject.addOneAct(0, 1, 1)
# myproject.addOneAct(0, 2, 2)
# myproject.addOneAct(2, 1, 3)
# myproject.addOneAct(1, 3, 4)
# myproject.addOneAct(3, 2, 5)

# for i in myproject.Activity:
# 	print i
# print myproject.EarstTime
# print myproject.InPoint
# print myproject.TopSort
PointNum, ActivityNum = map(int, raw_input().split())
myproject = DAG(PointNum)
for line in range(ActivityNum):
	p1, p2, time = map(int, raw_input().split())
	myproject.addOneAct(p1, p2, time)

if myproject.TopSorting():
	print max(myproject.EarstTime.values())
else:
	print 'Impossible'



