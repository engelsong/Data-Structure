
class MGraph(object):

    def __init__(self, maxVertexNum=1):
        self.Vertex = []
        self.Edge = [0 for i in range(maxVertexNum * (maxVertexNum - 1) / 2)]

    def addOneEdge(self, v1, v2, weight=1):
        i = max(v1, v2)
        j = min(v1, v2)
        self.Edge[i * (i - 1) / 2 + j] = weight

    def addOneVertex(self, VertexName):
        index = len(self.Vertex)
        self.Vertex.append(VertexName)
        return index

    def connectedVertex(self, Vertex):
        res = []
        for v in range(len(self.Vertex)):
            if v < Vertex:
                i, j = Vertex, v
            elif v > Vertex:
                i, j = v, Vertex
            else:
                continue
            if self.Edge[i * (i - 1) / 2 + j] == 1:
                res.append(v)
        return res

    def sixBFS(self, Vertex):
        res= []
        tail = None
        level = 0
        last = Vertex
        queue = [Vertex]
        while len(queue) != 0:
            temp = queue.pop(0)
            res.append(temp)
            for v in self.connectedVertex(temp):
                if v not in res and v not in queue:
                    queue.append(v)
                    tail = v
            if temp == last:
                level += 1
                last = tail
            if level == 7:
                break
        return res
    
    def showSDS(self):
        VerNums = len(self.Vertex)
        for eachV in self.Vertex:
            num = float(len(self.sixBFS(eachV)))
            print '{}: {:.2f}%'.format(eachV + 1, num / VerNums * 100)


# VerNum, EdgeNum = map(int, raw_input().split())
# sample = MGraph(VerNum)
# sample.Vertex = [v for v in range(VerNum)]
# for eachEdge in range(EdgeNum):
#     v1, v2 = map(int, raw_input().split())
#     sample.addOneEdge(v1 -1, v2 -1)

# sample.showSDS()




sn = MGraph(3)
sn.Vertex = [v for v in range(3)]
sn.addOneEdge(1, 2)
# sn.addOneEdge(2, 3)
# sn.addOneEdge(3, 4)
# sn.addOneEdge(4, 5)
# sn.addOneEdge(5, 6)
# sn.addOneEdge(6, 7)
# sn.addOneEdge(7, 8)
# sn.addOneEdge(8, 9)
# sn.addOneEdge(1, 0)
# print sn.Vertex
# print sn.sixBFS(0)
sn.showSDS()


