# coding=utf-8


class queue(object):

    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def isempty(self):
        isempty = 0
        if len(self.queue) == 0:
            isempty = 1
        return isempty

    def add(self, element):
        self.rear = self.rear + 1
        self.queue.append(element)

    def delete(self):
        if self.isempty():
            raise Exception("The queue is empty!")
        else:
            res = self.queue[0]
            self.queue.remove(res)
            return res

original = queue()
in_put = raw_input()


for i in in_put.split():
    original.add(int(i))

res = []
while not original.isempty():
    a = original.delete()
    b = original.delete()
    if b == 0:
    	continue 
    res.append(a * b)
    res.append(b - 1)
if len(res) == 0:
    print '0 0'
else:
    for i in res:
        print i,
