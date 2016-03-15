class AVLTree(object):

    def __init__(self):
        self.tree = {}
        self.root = None

    def FindRoot(self):
        '''find the right root for the tree'''
        root = None
        if len(self.tree) != 0:  # check the tree if it is empty
            fatherNodeSet = set(self.tree.keys())
            sonNodeSet = set()
            for i in self.tree.values():
                sonNodeSet.update(i[:2])
            # if one node is only in father node, it is root
            root = list(fatherNodeSet - sonNodeSet)[0]
            self.root = root
        return root

    def FindNode(self, node):
        '''return the father and index of the node'''
        if node == self.root:
            res = [None, None] #if the node is root
        else:
            temp = self.root #record the father node
            while temp is not None:
                if node > temp:
                    #big to right
                    if self.tree[temp][1] == node:
                        res = [temp, 1]
                        break
                    temp = self.tree[temp][1]
                elif node < temp:
                    #small to left
                    if self.tree[temp][0] == node:
                        res = [temp, 0]
                        break
                    temp = self.tree[temp][0]
            else:
                raise Exception("Doesn't exist")
        return res

    def GetHeight(self, node):
        '''calculate the absolute height of the given node, None is -1'''

        if node is None: 
            #if none return -1, the opposite height plus 1
            return -1
        elif self.tree[node][0] is None and self.tree[node][1] is None:
            #have no son node 
            return 0 
        elif self.tree[node][0] is None: # no left son , right plus 1
            return self.GetHeight(self.tree[node][1]) + 1
        elif self.tree[node][1] is None: #no right son, left plus 1
            return self.GetHeight(self.tree[node][0]) + 1
        else:
            #have both son node ,then find the bigger height of both
            return max(self.GetHeight(self.tree[node][1]), self.GetHeight(self.tree[node][0])) + 1

    def SingleLeftRo(self, node):
        '''single left rotate node and res, update their height'''
        # node(a) have to have a left subnode(res)
        pos = self.FindNode(node) #find the positon of the node
        res = self.tree[node][0] #record the left son of left node
        self.tree[node][0] = self.tree[res][1] 
        #put the right son to the left son of the node
        self.tree[res][1] = node 
        if pos[0] is not None: 
            #if the node has father node, connect it with new node-res
            self.tree[pos[0]][pos[1]] = res
        else:
            #if it is root, update root and do nothing
            self.root = res
        #update the height
        self.tree[node][2] = self.GetHeight(node)
        self.tree[res][2] = self.GetHeight(res)
        return res

    def SingleRightRo(self, node):
        #node have to have a right subnode - res
        pos = self.FindNode(node)
        res = self.tree[node][1]
        self.tree[node][1] = self.tree[res][0]
        self.tree[res][0] = node
        if pos[0] is not None:
            self.tree[pos[0]][pos[1]] = res
        else:
            self.root = res
        self.tree[node][2] = self.GetHeight(node)
        self.tree[res][2] = self.GetHeight(res)
        return res

    def LeftRightRo(self, node): 
        '''the node(a) must have a left son node(b), 
        and the left son node must have a right son node(c)'''
        # right rotate b, give c to left
        self.tree[node][0] = self.SingleRightRo(self.tree[node][0])
        # left rotate a ,return c, 
        return self.SingleLeftRo(node)

    def RightLeftRo(self, node):
        self.tree[node][1] = self.SingleLeftRo(self.tree[node][1])
        return self.SingleRightRo(node)

    def CheckBalFactor(self, node):
        '''check the balence factor for the given node,
        left height minus right, positive means left tree is high'''
        res = self.GetHeight(
            self.tree[node][0]) - self.GetHeight(self.tree[node][1])
        return res

    def Insert(self, node):
        if len(self.tree) == 0:
            self.tree[node] = [None, None, 0]
            self.root = node
            return self.root
        else:
            stack = [] #record the path to the right place
            temp = self.root
            while True:  # start from root and search for the right place
                stack.append(temp)
                if node > temp:
                    if self.tree[temp][1] is None:
                        self.tree[temp][1] = node
                        self.tree[temp][2] += 1
                        self.tree[node] = [None, None, 0]
                        stack.append(node)
                        break
                    self.tree[temp][2] += 1
                    temp = self.tree[temp][1]  # bigger to right
                elif node < temp:
                    if self.tree[temp][0] is None:
                        self.tree[temp][0] = node
                        self.tree[temp][2] += 1
                        self.tree[node] = [None, None, 0]
                        stack.append(node)
                        break
                    self.tree[temp][2] += 1
                    temp = self.tree[temp][0]  # small to left
                elif node == temp:
                    return self.root

            depth = len(stack)
            stack = stack[::-1] #revers the path
            for i in range(depth): 
                #from the leaf to the root check the balance factor
                factor = self.CheckBalFactor(stack[i])
                if factor == 2: #the left tree is too high
                    if stack[i - 1] > stack[i - 2]: 
                    # the trouble node is at the left son node 
                        self.SingleLeftRo(stack[i])
                    else:
                    #the trouble node is at the right son node 
                        self.LeftRightRo(stack[i])
                elif factor == -2: #the right tree is too high
                    if stack[i - 1] < stack[i - 2]:
                    #at right son node
                        self.SingleRightRo(stack[i])
                    else:
                    #at left son node
                        self.RightLeftRo(stack[i])
                self.tree[stack[i]][2] = self.GetHeight(stack[i])
            return self.root

    def Plot(self):
        lst = [[self.root]]
        for i in range(self.tree[self.root][2]):
            tempLst = []
            for j in lst[i]:
                tempLst += self.tree[j][:2]
            lst.append(tempLst)
        n = len(lst)
        res = []
        for x in range(n):
            temp = ' ' * (2 ** abs(x - n + 1) - 1)
            for y in range(len(lst[x])):
                if y + 1 == len(lst[x]):
                    temp += str(lst[x][y])
                else:    
                    temp += str(lst[x][y]) + ' ' * (2 ** abs(x - n) - 1)
            res.append(temp)

        for z in res:
            print z

def check(tree1, tree2):
    if tree1.tree == tree2.tree:
        print 'Yes'
    else:
        print 'No'


while 1:
    userin = raw_input()
    if userin == '0':
        break
    N, L = map(int, userin.split())
    oritree = AVLTree()
    treeNodes = map(int, raw_input().split())
    for node in treeNodes:
        oritree.Insert(node)
    for l in range(L):
        temp = AVLTree()
        treeNodes = map(int, raw_input().split())
        for node in treeNodes:
            temp.Insert(node)
        check(oritree, temp)

