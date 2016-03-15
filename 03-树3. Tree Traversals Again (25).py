class BiTree(object):

    def __init__(self):
        self.tree = {}
        self.root = None

    def addOneNode(self, data, left=None, right=None):
        self.tree[data] = [left, right]

    def setRoot(self, root, left=None, right=None):
        if root not in self.tree.keys():
            self.root = root
            self.tree[root] = [left, right]
        else:
            self.root = root

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

    def PreOderTrav(self, root):
        if root != None:
            print root,
            self.PreOderTrav(self.tree[root][0])
            self.PreOderTrav(self.tree[root][1])

    def InOderTrav(self, root):
        if root != None:
            self.InOderTrav(self.tree[root][0])
            print root,
            self.InOderTrav(self.tree[root][1])

    def PostOrderTrav(self, root):
        if root != None:
            self.PostOrderTrav(self.tree[root][0])
            self.PostOrderTrav(self.tree[root][1])
            print root,

    def LevelOrderTrav(self):
        if self.findRoot() == None:
            return None
        else:
            queue = []
            queue.append(self.root)
            while len(queue) != 0:
                temp = queue[0]
                queue.remove(temp)
                left, right = self.tree[temp][0], self.tree[temp][1]
                print temp,
                if left != None:
                    queue.append(left)
                if right != None:
                    queue.append(right)


tree1 = BiTree()
dict = {}
num = int(raw_input())
for i in range(num):
    dict[str(i + 1)] = [None, None]
inputLast = None
inputNow = None
popLast = None
stack = []
for j in range(2 * num):
    inputNow = raw_input().split()
    if inputLast == None: #the first input must be push ,and the node must be root
        tree1.setRoot(inputNow[1])
        stack.append(inputNow[1])
        
    elif inputLast[0] == 'Push': 
        if inputNow[0] == "Push": 
        #two push in a roll means the second node is the left son node of last
            dict[inputLast[1]][0] = inputNow[1]
            stack.append(inputNow[1])
        elif inputNow[0] == 'Pop': 
            #the pop after push means the poped node have no left son node
            popLast = stack[-1]            
            stack.remove(popLast)
    elif inputLast[0] == 'Pop':
        if inputNow[0] == "Push":
            #the push node after pop means the pushed node is the right son of poped node 
            dict[popLast][1] = inputNow[1]
            stack.append(inputNow[1])
        elif inputNow[0] == 'Pop':
            #two pop in a roll means, last poped node has no right son
            popLast = stack[-1]
            stack.remove(popLast)
    inputLast = inputNow
    

tree1.initTreeWithDict(dict)
tree1.PostOrderTrav(tree1.root)
