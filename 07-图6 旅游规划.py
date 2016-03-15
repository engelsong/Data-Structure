class RoadMap(object):

    def __init__(self, maxCityNum=1):
        self.city = [i for i in range(maxCityNum)]
        self.road = [[0 for i in range(maxCityNum)]
                     for i in range(maxCityNum)]

        self.tolls = [[0 for i in range(maxCityNum)]
                      for i in range(maxCityNum)]

    def addOneRoad(self, v1, v2, weight=1, cost=1):
        self.road[v1][v2] = weight
        self.road[v2][v1] = weight
        self.tolls[v1][v2] = cost
        self.tolls[v2][v1] = cost

    def connectedCitys(self, city):
        res = []
        for v in range(len(self.city)):
            if self.road[city][v] != 0:
                res.append(v)
        return res

    def Djikstra(self, city):
        infi = float('inf')
        collected = set()
        path = [None for i in range(len(self.city))]
        dist = [infi for i in range(len(self.city))]
        toll = [infi for i in range(len(self.city))]
        dist[city] = 0
        toll[city] = 0
        while 1:
            allcity = set(range(len(dist)))
            UnCollected = allcity ^ collected
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
            for W in self.connectedCitys(V):
                if W not in collected:
                    if dist[V] + self.road[V][W] < dist[W]:
                        dist[W] = dist[V] + self.road[V][W]
                        toll[W] = toll[V] + self.tolls[V][W]
                        path[W] = V
                    elif dist[V] + self.road[V][W] == dist[W] and toll[V] + self.tolls[V][W] < toll[W]:
                        toll[W] = toll[V] + self.tolls[V][W]
                        path[W] = V

        return dist, toll

firstline = map(int, raw_input().split())

# InPut = '''0 1 1 20
# 1 3 2 30
# 0 3 4 10
# 0 2 2 20
# 2 3 1 20'''.split('\n')


TheMap = RoadMap(firstline[0])
# for i in InPut:
#     temp = map(int, i.split())
#     TheMap.addOneRoad(temp[0], temp[1], temp[2], temp[3])
for i in range(firstline[1]):
    temp = map(int, raw_input().split())
    TheMap.addOneRoad(temp[0], temp[1], temp[2], temp[3])
dist, toll = TheMap.Djikstra(firstline[2])
print dist[firstline[3]], toll[firstline[3]]
