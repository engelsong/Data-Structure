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





