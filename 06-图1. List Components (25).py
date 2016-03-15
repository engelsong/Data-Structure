class MGraph(object):

    def __init__(self, maxVertexNum=1):
        self.Vertex = [i for i in range(maxVertexNum)]
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

    def DFS(self, Vertex):
        '''start from Vertex, return depth frist search'''
        res = []

        def visit(x):
            res.append(x)
            for v in self.connectedVertex(x):
                if v not in res:
                    visit(v)
        visit(Vertex)
        return res

    def totalDFS(self):
        '''start form the fisrt vertex, return a list'''
        visted = []
        res = []
        for v in self.Vertex:
            if v not in visted:
                temp = self.DFS(v)
                res.append(temp)
                visted += temp
        return res

    def BFS(self, Vertex):
        res = []
        queue = [Vertex]
        while len(queue) != 0:
            temp = queue.pop(0)
            res.append(temp)
            for v in self.connectedVertex(temp):
                if v not in res and v not in queue:
                    queue.append(v)
        return res

    def totalBFS(self):
        visited = []
        res = []
        for v in self.Vertex:
            if v not in visited:
                temp = self.BFS(v)
                res.append(temp)
                visited += temp
        return res

    def showRes(self):
        for i in self.totalDFS():
            print '{ '+' '.join(map(str,i)) + ' }'
        for j in self.totalBFS():
            print '{ '+' '.join(map(str,j)) + ' }'

firstInputLine = map(int, raw_input().split())
maxVertexNum, edgeNums = firstInputLine
myMGraph = MGraph(maxVertexNum)

for eachLine in range(edgeNums):
    InputLine = map(int, raw_input().split())
    v1, v2 = InputLine
    myMGraph.addOneEdge(v1, v2)

myMGraph.showRes()

