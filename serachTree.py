class SearchTree(object):

    def __init__(self):
        self.tree = {}
        self.root = None

    def InsertOneNode(self, data):
        '''insert on node in the tree'''
        if len(self.tree) == 0:  # if the tree is empty, then insert the node ,and set it as root
            self.tree[data] = [None, None, 0]
            self.root = data
        else:
            temp = self.root
            while True:  # start from root and search for the right place
                if data > temp:
                    if self.tree[temp][1] is None:
                        self.tree[temp][1] = data
                        self.tree[data] = [None, None, 0]
                        break
                    temp = self.tree[temp][1]  # bigger to right
                elif data < temp:
                    if self.tree[temp][0] is None:
                        self.tree[temp][0] = data
                        self.tree[data] = [None, None, 0]
                        break
                    temp = self.tree[temp][0]  # small to left
                elif data == temp:
                    raise Exception('The Node alreaday exists in the tree')

    def Delete(self, node):
        ''' delete the node''' #check the find method
        if node not in self.tree:
            return ('The node doesn\'t exist')
        else:
            FNode, Pos = self.FindNode(node)
            if self.tree[node][0] is not None and self.tree[node][1] is not None:
                if node is not self.root:
                    self.tree[FNode][Pos] = None
                nodes = self.LevelOrderTrav(node)
                for i in nodes:
                    del self.tree[i]
                for j in nodes[1:]:
                    self.InsertOneNode(j)

            else:
                if self.tree[node][0] is None:
                    self.tree[FNode][Pos] = self.tree[node][1]
                else:
                    # self.tree[node][1] is None:
                    self.tree[FNode][Pos] = self.tree[node][0]
                del self.tree[node]


    def FindNode(self, node):
        '''return the father and index of the node'''
        if node == self.root:
            res = [None, None]
        else:
            temp = self.root
            while temp is not None:
                if node > temp:
                    if self.tree[temp][1] == node:
                        res = [temp, 1]
                        break
                    temp = self.tree[temp][1]
                elif node < temp:
                    if self.tree[temp][0] == node:
                        res = [temp, 0]
                        break
                    temp = self.tree[temp][0]
            else:
                raise Exception('Doesn\'t exist')
        return res

    def FindMin(self, node):
        temp = node
        while temp is not None:
            res = temp
            temp = self.tree[temp][0]
        return res

    def FindMax(self, node):
        temp = node
        while temp is not None:
            res = temp
            temp = self.tree[temp][1]
        return res

    def LevelOrderTrav(self, start):
        res = []
        queue = []
        queue.append(start)
        while len(queue) != 0:
            temp = queue[0]
            queue.remove(temp)
            left, right = self.tree[temp][0], self.tree[temp][1]
            res.append(temp)
            if left != None:
                queue.append(left)
            if right != None:
                queue.append(right)
        return res


MyTree = SearchTree()
MyTree.InsertOneNode(5)
MyTree.InsertOneNode(2)
MyTree.InsertOneNode(3)
MyTree.InsertOneNode(1)
MyTree.InsertOneNode(8)
MyTree.InsertOneNode(6)
MyTree.InsertOneNode(10)
print MyTree.tree
MyTree.Delete(5)
print MyTree.tree
print MyTree.LevelOrderTrav(MyTree.root)
