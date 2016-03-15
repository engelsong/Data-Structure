

class DGraph(object):

    def __init__(self, maxVertexNum=1):
        self.Vertex = [i for i in range(maxVertexNum)]
        self.Edge = [[0 for i in range(maxVertexNum)]
                     for i in range(maxVertexNum)]
        self.dist = [[float('inf') for i in range(maxVertexNum)]
                     for i in range(maxVertexNum)]
        self.path = [[-1 for i in range(maxVertexNum)]
                     for i in range(maxVertexNum)]

    def addOneVertex(self, VertexName):
        index = self.Vertex.index(None)
        self.Vertex[index] = VertexName
        return index

    def addOneEdge(self, v1, v2, weight=1):
        self.Edge[v1][v2] = weight
        self.Edge[v2][v1] = weight


    def connectedVertex(self, Vertex):
        res = []
        for v in range(len(self.Vertex)):
            if self.Edge[Vertex][v] != 0:
                res.append(v)
        return res


    def Floyd(self):
        for i in self.Vertex:
            for j in self.Vertex:
                if self.Edge[i][j] != 0 or i == j:
                    self.dist[i][j] = self.Edge[i][j]
        for k in self.Vertex:
            for i in self.Vertex:
                for j in self.Vertex:
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.path[i][j] = k


firstline = raw_input().split()
VertexNum = int(firstline[0])
edgeNum = int(firstline[1])

thegraph = DGraph(VertexNum)
for i in range(edgeNum):
    temp = map(int, raw_input().split())
    thegraph.addOneEdge(temp[0] - 1, temp[1] - 1, temp[2])


# firstline = '6 11'
# In = '''3 4 70
# 1 2 1
# 5 4 50
# 2 6 50
# 5 6 60
# 1 3 70
# 4 6 60
# 3 6 80
# 5 1 100
# 2 4 60
# 5 2 80'''.split('\n')
# # VertexNum, EdgeNum = map(int, firstline.split())
# thegraph = DGraph(6)
# for i in In:
#     temp = i.split()
#     thegraph.addOneEdge(int(temp[0]) - 1, int(temp[1]) - 1, int(temp[2]))


thegraph.Floyd()

eachMax = []
for i in thegraph.dist:
    eachMax.append(max(i))

theMinNum = min(eachMax)

if theMinNum == float('inf'):
    print 0
else:    
    code = eachMax.index(theMinNum)
    print code + 1, max(thegraph.dist[code])

