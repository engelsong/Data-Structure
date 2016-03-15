class FUSet(object):

    """docstring for FUSet"""

    def __init__(self):
        self.data = []
        self.parent = []

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
                # self.data.append(item2)
                # self.parent.append(root1)
                self.parent[root1] -= 1
        else:
            # self.data.append(item1)
            # self.parent.append(-1)
            index1 = self.data.index(item1)
            if root2 != -1:
                self.parent[index1] = root2
                self.parent[root2] -= 1
            else:
                # self.data.append(item2)
                # self.parent.append(-1)
                index2 = self.data.index(item2)
                self.parent[index2] = index1
                self.parent[index1] -= 1

    def ShowSet(self):
        for i in self.data:
            print '{:>2}'.format(i),
        print
        for j in self.parent:
            print '{:>2}'.format(j),
        print


myset = FUSet()
myset.data = [x for x in range(1,6)]
myset.parent = [-1 for i in range(5)] 
myset.ShowSet()
myset.Union(3, 2)
myset.Union(1, 3)
myset.Union(4, 5)
myset.Union(3, 4)
myset.ShowSet()
# print myset.Find('1')
# print myset.Find('5')