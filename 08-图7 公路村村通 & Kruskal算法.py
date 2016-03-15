class MinHeap(object):

    def __init__(self, MinData=0):
        self.Size = 0
        self.Data = [(0, 0)]
        self.Dict = {(0, 0): 0}

    def IsEmpty(self):
        res = False
        if self.Size == 0:
            res = True
        return res

    def Comp(self, item1, item2):
        res = False
        if self.Dict[item1] > self.Dict[item2]:
            res = True
        return res

    def Insert(self, item, weight):
        self.Dict[item] = weight
        if self.IsEmpty():
            self.Data.append(item)
            self.Size += 1
        else:
            self.Size += 1
            self.Data.append(item)
            pos = self.Size
            while self.Comp(self.Data[pos / 2], item):
                self.Data[pos] = self.Data[pos / 2]
                pos /= 2
            self.Data[pos] = item

    def Delete(self):
        if self.IsEmpty():
            raise Exception("the heap is empty!")
        res = self.Data[1]
        weight = self.Dict.pop(res)
        temp = self.Data.pop(self.Size)
        self.Size -= 1
        parent = 1
        child = parent * 2
        while child <= self.Size:
            if child != self.Size and self.Comp(self.Data[child], self.Data[child + 1]):
                child += 1
            if self.Comp(self.Data[child], temp):
                break
            else:
                self.Data[parent] = self.Data[child]
                parent = child
                child = parent * 2
        if not self.IsEmpty():
            self.Data[parent] = temp
        return res, weight


class FUSet(object):

    def __init__(self, Num):
        self.data = [i for i in range(Num)]
        self.parent = [-1 for i in range(Num)]

    def Find(self, item):
        res = None
        if item not in self.data:
            res = -1
            self.data.append(item)
            self.parent.append(-1)
        else:
            index = self.data.index(item)
            while self.parent[index] >= 0:
                index = self.parent[index]
            res = index
        return res

    def Union(self, item1, item2):
        root1 = self.Find(item1)
        root2 = self.Find(item2)
        if root1 != -1:
            if root2 != -1:
                if self.parent[root1] >= self.parent[root2]:
                    if self.parent[root1] < 0:
                        temp = self.parent[root1]
                        self.parent[root1] = root2
                        self.parent[root2] += temp
                elif self.parent[root1] < self.parent[root2]:
                    temp = self.parent[root2]
                    self.parent[root2] = root1
                    self.parent[root1] += temp
            else:
                self.parent[root1] -= 1
        else:
            index1 = self.data.index(item1)
            if root2 != -1:
                self.parent[index1] = root2
                self.parent[root2] -= 1
            else:
                index2 = self.data.index(item2)
                self.parent[index2] = index1
                self.parent[index1] -= 1

    def Check(self, item1, item2):
        res = False
        root1 = self.Find(item1)
        root2 = self.Find(item2)
        if root1 != root2:
            self.Union(item1, item2)
            res = True
        return res




class DGraph(object):

    def __init__(self, maxVertexNum=1):
        self.maxVertexNum = maxVertexNum
        self.Vertex = [i for i in range(maxVertexNum)]
        self.Edge = [[0 for i in range(maxVertexNum)]
                     for i in range(maxVertexNum)]
        self.EdgeHeap = MinHeap()
        self.TheSet = FUSet(maxVertexNum)

    def addOneEdge(self, v1, v2, weight=1):
        self.Edge[v1][v2] = weight
        self.Edge[v2][v1] = weight
        self.EdgeHeap.Insert((v1, v2), weight)

    def connectedVertex(self, Vertex):
        res = []
        for v in range(len(self.Vertex)):
            if self.Edge[Vertex][v] != 0:
                res.append(v)
        return res

    def Kruskal(self):
        MST=[]
        res = 0
        while len(MST) < self.maxVertexNum - 1 and not self.EdgeHeap.IsEmpty():
            temp, weight = self.EdgeHeap.Delete()
            if self.TheSet.Check(temp[0], temp[1]):
                MST.append(temp)
                res += weight
        if len(MST) < self.maxVertexNum - 1:
            return -1
        else:
            return res

# mygraph = DGraph(7)
# mygraph.addOneEdge(0, 3, 1)
# mygraph.addOneEdge(1, 3, 3)
# mygraph.addOneEdge(3, 4, 7)
# mygraph.addOneEdge(3, 6, 4)
# mygraph.addOneEdge(3, 5, 8)
# mygraph.addOneEdge(2, 3, 2)
# mygraph.addOneEdge(0, 1, 2)
# mygraph.addOneEdge(1, 4, 10)
# mygraph.addOneEdge(4, 6, 6)
# mygraph.addOneEdge(5, 6, 1)
# mygraph.addOneEdge(2, 5, 5)
# mygraph.addOneEdge(0, 2, 4)
# mygraph.addOneEdge(4, 7, 2)
maxVertexNum, EdgeNum = map(int, raw_input().split())
mygraph = DGraph(maxVertexNum)
for i in range(EdgeNum):
    v1, v2, weight = map(int, raw_input().split())
    mygraph.addOneEdge(v1 - 1, v2 -1, weight)
print mygraph.Kruskal()
