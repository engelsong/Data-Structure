class BiTree(object):

    def __init__(self):
        self.tree = {}
        self.root = None

    def findRoot(self):
        root = None
        if self.root == None:
            if len(self.tree) != 0:
                fatherNodeSet = set(self.tree.keys())
                sonNodeSet = set()
                for i in self.tree.values():
                    sonNodeSet.update(i)

                root = list(fatherNodeSet - sonNodeSet)[0]
                self.root = root

        else:
            root = self.root

        return root

    def initTreeWithDict(self, dict):
        self.tree = dict

    

    def pfLeafs(self):
        if self.findRoot() == None: #if the tree is empty
            return None
        else:
            queue = [] 
            queue.append(self.root) #put the root in 
            while len(queue) != 0:
                temp = queue[0] #choose the frist element in queue
                queue.remove(temp) 
                left, right = self.tree[temp][0], self.tree[temp][1] #find the left and right son node
                if left == None and right == None: #if it has no son, print it
                    print temp,
                if left != None: #put his son in queue
                    queue.append(left)
                if right != None:
                    queue.append(right)


dict = {}
num = int(raw_input())
for i in range(num):
    temp = raw_input().split()
    value = []
    for j in temp:
        if j == '-':
            value.append(None)
        else:
            value.append(int(j))
    dict[i] = value


tree1 = BiTree()
tree1.initTreeWithDict(dict)
tree1.findRoot()
tree1.pfLeafs()
