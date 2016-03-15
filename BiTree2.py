class BiTree(object):

    '''create a binary tree with dictionary.
    key is the node ,taking a list as value. 
    each list has two element, first one is left ,another is right'''

    def __init__(self):
        self.tree = {}  # the tree
        self.root = None  # the root

    def addOneNode(self, data, left=None, right=None):
        '''add one node in the tree, 
        the left node and the right node are defaultly set to be None'''
        self.tree[data] = [left, right]

    def setRoot(self, root, left, right):
        '''set one node as the root of the tree'''
        if root not in self.tree.keys():
            self.root = root
            self.tree[root] = [left, right]
        else:
            self.root = root

    def findRoot(self):
        '''in case you initial the tree with a dictionary.
        and you havn't set a root for it, you can use this method find the root of it'''
        root = None
        # if the root of the tree has't been set, find it
        if self.root == None:
            if len(self.tree) != 0:  # check the tree if it is empty
                fatherNodeSet = set(self.tree.keys())
                sonNodeSet = set()
                for i in self.tree.values():
                    sonNodeSet.update(i)
                # if one node is only in father node, it is root
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

    def InOderTrav(self):
        res = []
        root = self.root
        tree = self.tree

        def Trav(tree, root):
            if root != None:
                Trav(tree, tree[root][0])
                res.append(root)
                Trav(tree, tree[root][1])
        Trav(tree, root)
        return res

    def PostOrderTrav(self):
        res = []
        root = self.root
        tree = self.tree

        def Trav(tree, root):
            if root != None:
                Trav(tree, tree[root][0])
                Trav(tree, tree[root][1])
                res.append(root)
        Trav(tree, root)
        return res

    def LevelOrderTrav(self):
        res = []
        if self.findRoot() == None:
            return None
        else:
            queue = []
            queue.append(self.root)
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

    def pfLeafs(self):
        if self.findRoot() == None:
            return None
        else:
            queue = []
            queue.append(self.root)
            while len(queue) != 0:
                temp = queue[0]
                queue.remove(temp)
                left, right = self.tree[temp][0], self.tree[temp][1]
                if left == None and right == None:
                    print temp,
                if left != None:
                    queue.append(left)
                if right != None:
                    queue.append(right)


tree1 = BiTree()

dict = {'a': ['b', 'c'], 'b': ['d', 'f'], 'c': ['g', 'i'], 'd': [None, None],
        'e': [None, None], 'f': ['e', None], 'g': [None, 'h'], 'h': [None, None], 'i': [None, None]}


tree1.initTreeWithDict(dict)
tree1.findRoot()
print tree1.LevelOrderTrav()
