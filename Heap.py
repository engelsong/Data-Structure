class MaxHeap(object):

    def __init__(self, MaxData=10e10):
        self.MaxData = MaxData
        self.Data = [MaxData]
        self.Size = 0

    def IsEmpty(self):
        res = False
        if self.Size == 0:
            res = True
        return res

    def Insert(self, item):
        if item > self.MaxData:
            raise IOError("Out of the heap's range")
        self.Size += 1  # update size
        self.Data.append(item)  # put it in the last
        pos = self.Size
        # find the father, if the father is small, change
        while self.Data[pos / 2] < item:
            self.Data[pos] = self.Data[pos / 2]
            pos = pos / 2
        self.Data[pos] = item

    def Delete(self):
        if self.IsEmpty():
            raise Exception('The heap is empty!')
        res = self.Data[1]  # return the biggest one
        temp = self.Data.pop(self.Size)  # take the last one to the top
        self.Size -= 1  # update size
        parent = 1  # set the parent node
        child = parent * 2
        while child <= self.Size:
            # if there is child
            if child < self.Size:
                if self.Data[child] < self.Data[child + 1]:
                    # find the bigger one in left and right child
                    child += 1
            if temp >= self.Data[child]:  # if the node bigger than all child
                break
            else:
                # take the child to parent
                self.Data[parent] = self.Data[child]
                parent = child  # update parent node
                child = parent * 2  # find new child
        if not self.IsEmpty():
            self.Data[parent] = temp
        return res

    def PrintData(self):
        print self.Data[1:]

    def InitWithList(self, lst):
        '''change a lst into MaxHeap'''
        lst = [self.MaxData] + lst
        self.Size = len(lst) - 1
        path = range(1, len(lst) / 2 + 1)[::-1]
        for i in path:
            parent = i
            child = parent * 2
            while child <= self.Size:
                if child != self.Size:
                    if lst[child] < lst[child + 1]:
                        # find the bigger one in left and right child
                        child += 1
                if lst[parent] > lst[child]:
                    break
                else:
                    temp = lst[child]
                    lst[child] = lst[parent]
                    lst[parent] = temp
                    parent = child
                    child = parent * 2
        self.Data = lst
        return self.Data


class MinHeap(object):

    """return the smallest one of the heap"""

    def __init__(self, MinData=-10e10):
        self.Size = 0
        self.Data = [MinData]
        self.MinData = MinData

    def IsEmpty(self):
        res = False
        if self.Size == 0:
            res = True
        return res

    def Insert(self, item):
        if item < self.MinData:
            raise IOError("Out of the heap's range")
        self.Size += 1
        pos = self.Size
        self.Data.append(item)
        while self.Data[pos / 2] > item:
            self.Data[pos] = self.Data[pos / 2]
            pos /= 2
        self.Data[pos] = item

    def Delete(self):
        if self.IsEmpty():
            raise Exception("the heap is empty!")
        res = self.Data[1]
        temp = self.Data.pop(self.Size)
        self.Size -= 1
        parent = 1
        child = parent * 2
        while child <= self.Size:
            if child != self.Size and self.Data[child] > self.Data[child + 1]:
                child += 1
            if temp < self.Data[child]:
                break
            else:
                self.Data[parent] = self.Data[child]
                parent = child
                child = parent * 2
        if not self.IsEmpty():
            self.Data[parent] = temp
        return res

    def PrintData(self):
        print self.Data[1:]

    def InitWithList(self, lst):
        '''change a lst into MinHeap'''
        lst = [self.MinData] + lst
        self.Size = len(lst) - 1
        path = range(1, self.Size / 2 + 1)[::-1]
        for i in path:
            parent = i
            child = parent * 2
            while child <= self.Size:
                if child != self.Size:
                    if lst[child] > lst[child + 1]:
                        # find the smaller one in left and right child
                        child += 1
                if lst[parent] < lst[child]:
                    break
                else:
                    temp = lst[child]
                    lst[child] = lst[parent]
                    lst[parent] = temp
                    parent = child
                    child = parent * 2
        self.Data = lst
        return self.Data

lst = [1, 3, 6, 0, 2, 8, 5, 9, 7, 4]

myheap1 = MaxHeap()
myheap2 = MinHeap()

# myheap2.Insert(25)
# myheap2.Insert(58)
# myheap2.Insert(20)

myheap1.InitWithList(lst)
myheap2.InitWithList(lst)

myheap1.PrintData()
myheap2.PrintData()
# print myheap2.Size


