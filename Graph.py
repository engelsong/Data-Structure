# coding: UTF-8
class UDGraph(object):

    '''邻接矩阵表示无相图'''

    def __init__(self, maxVertexNum=1):
        self.Vertex = [None for i in range(maxVertexNum)]
        self.Edge = [0 for i in range(maxVertexNum * (maxVertexNum - 1) / 2)]

    def addOneEdge(self, v1, v2, weight=1):
        i = max(v1, v2)
        j = min(v1, v2)
        self.Edge[i * (i - 1) / 2 + j] = weight

    def addOneVertex(self, VertexName):
        index = self.Vertex.index(None)
        self.Vertex[index] = VertexName
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
            if self.Edge[i * (i - 1) / 2 + j] != 0:
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

    def UWPath(self, Vertex):
        '''无权最短路径'''
        path = [None for i in range(len(self.Vertex))]
        dist = [-1 for i in range(len(self.Vertex))]
        dist[Vertex] = 0
        queue = [Vertex]
        while len(queue) != 0:
            temp = queue.pop(0)
            for v in self.connectedVertex(temp):
                if dist[v] == -1:
                    dist[v] = dist[temp] + 1
                    path[v] = temp
                    queue.append(v)
        return dist, path


class DGraph(object):

    '''邻接矩阵表示有相图'''

    def __init__(self, maxVertexNum=1):
        self.Vertex = [None for i in range(maxVertexNum)]
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

    def connectedVertex(self, Vertex):
        res = []
        for v in range(len(self.Vertex)):
            if self.Edge[Vertex][v] != 0:
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

    def UWPath(self, Vertex):
        '''无权最短路径'''
        path = [None for i in range(len(self.Vertex))]
        dist = [-1 for i in range(len(self.Vertex))]
        dist[Vertex] = 0
        queue = [Vertex]
        while len(queue) != 0:
            temp = queue.pop(0)
            for v in self.connectedVertex(temp):
                if dist[v] == -1:
                    dist[v] = dist[temp] + 1
                    path[v] = temp
                    queue.append(v)
        return dist, path

    def Djikstra(self, Vertex):
        '''单源有权最短路'''
        infi = float('inf')
        collected = set()
        path = [None for i in range(len(self.Vertex))]
        dist = [infi for i in range(len(self.Vertex))]
        dist[Vertex] = 0
        while 1:
            allVertex = set(range(len(dist)))
            UnCollected = allVertex ^ collected
            if len(UnCollected) == 0:
                break
            V = None
            temp = infi
            for x in UnCollected:
                if dist[x] < temp:
                    temp = dist[x]
                    V = x
            if V == None:
                break
            collected.add(V)
            for W in self.connectedVertex(V):
                if W not in collected:
                    if dist[V] + self.Edge[V][W] < dist[W]:
                        dist[W] = dist[V] + self.Edge[V][W]
                        path[W] = V
        return dist, path

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

    def Prim(self):
        infi = float('inf')
        dist = [infi for i in range(len(self.Vertex))]
        MST = [infi for i in range(len(self.Vertex))]
        MST[0] = -1
        collected = set()
        dist[0] = 0
        while 1:
            allVertex = set(range(len(self.Vertex)))
            UnCollected = allVertex ^ collected
            if len(UnCollected) == 0:
                break
            V = None
            temp = infi
            for x in UnCollected:
                if dist[x] < temp:
                    temp = dist[x]
                    V = x
            if V == None:
                raise EOFError('The MST does not exsit!')
            collected.add(V)
            dist[V] = 0
            for W in self.connectedVertex(V):
                if W not in collected:
                    if dist[V] + self.Edge[V][W] < dist[W]:
                        dist[W] = self.Edge[V][W]
                        MST[W] = V
        return MST

    def Kruskal(self):
        pass








mygraph = DGraph(7)
'老师的例子，232排列，顺序从上到下从左到右'
for i in range(7):
    mygraph.addOneVertex(i)
mygraph.addOneEdge(0, 1, 2)
mygraph.addOneEdge(0, 3, 1)
mygraph.addOneEdge(0, 2, 4)
mygraph.addOneEdge(1, 0, 2)
mygraph.addOneEdge(1, 3, 3)
mygraph.addOneEdge(1, 4, 10)
mygraph.addOneEdge(2, 0, 4)
mygraph.addOneEdge(2, 3, 2)
mygraph.addOneEdge(2, 5, 5)
mygraph.addOneEdge(3, 0, 1)
mygraph.addOneEdge(3, 1, 3)
mygraph.addOneEdge(3, 2, 2)
mygraph.addOneEdge(3, 4, 7)
mygraph.addOneEdge(3, 5, 8)
mygraph.addOneEdge(3, 6, 4)
mygraph.addOneEdge(4, 1, 10)
mygraph.addOneEdge(4, 3, 7)
mygraph.addOneEdge(4, 6, 6)
mygraph.addOneEdge(5, 2, 5)
mygraph.addOneEdge(5, 3, 8)
mygraph.addOneEdge(5, 6, 1)
mygraph.addOneEdge(6, 3, 4)
mygraph.addOneEdge(6, 4, 6)
mygraph.addOneEdge(6, 5, 1)




# print mygraph.connectedVertex(4)
# print mygraph.Djikstra(0)
# mygraph.Floyd()
# print 'edge is ', mygraph.Edge
# print 'dist is ',mygraph.dist
# print 'path is ',mygraph.pathmygraph.Prim()
print mygraph.Prim()



