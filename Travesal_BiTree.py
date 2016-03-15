

class stack(object):

    def __init__(self, size):
        self.stack = []
        self.top = -1
        self.size = size

    def isempty(self):
        isempty = 0
        if self.top == -1:
            isempty = 1
        return isempty

    def isfull(self):
        isfull = 0
        if self.top == self.size - 1:
            isfull = 1
        return isfull

    def push(self, element):
        if self.isfull():
            raise Exception("The stack is full!")
        else:
            self.top = self.top + 1
            self.stack.append(element)

    def pop(self):
        if self.isempty():
            raise Exception("The stack is empty!")
        else:
            self.top = self.top - 1
            return self.stack.pop()


class queue(object):

    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def isempty(self):
        isempty = 0
        if len(self.queue) == 0:
            isempty = 1
        return isempty

    def isfull(self):
        isfull = 0
        if len(self.queue) == self.size:
            isfull = 1
        return isfull

    def add(self, element):
        if self.isfull():
            raise Exception("The queue is full!")
        else:
            self.rear = self.rear + 1
            self.queue.append(element)

    def delete(self):
        if self.isempty():
            raise Exception("The queue is empty!")
        else:
            res = self.queue[0]
            self.queue.remove(res)
            return res


class BiTree(object):  # binary tree class

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def getDate(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def isEmpty(self):
        isEmpty = False
        if self.data == None:
            isEmpty = True
        return isEmpty


def PreOderTrav(BT):
    if BT != None:
        print BT.data,
        PreOderTrav(BT.left)
        PreOderTrav(BT.right)


def InOderTrav(BT):
    if BT != None:
        InOderTrav(BT.left)
        print BT.data,
        InOderTrav(BT.right)


def PostOrderTrav(BT):
    if BT != None:
        PostOrderTrav(BT.left)
        PostOrderTrav(BT.right)
        print BT.data,

# A = B = C = D = E = F = G = H = I = BiTree()


H = BiTree('H')
I = BiTree('I')
G = BiTree('G', None, H)
D = BiTree('D')
E = BiTree('E')
F = BiTree('F', E)
C = BiTree('C', G, I)
B = BiTree('B', D, F)
A = BiTree('A', B, C)

PreOderTrav(A)
print
InOderTrav(A)
print
PostOrderTrav(A)
