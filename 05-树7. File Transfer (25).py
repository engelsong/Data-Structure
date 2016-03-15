class network(object):

    def __init__(self, num):
        self.computers = [0] + [-1 for x in range(num)]

    def findroot(self, item):
        index = item
        while self.computers[index] > 0:
            index = self.computers[index]
        return index

    def union(self, c1, c2):
        root1 = self.findroot(c1)
        root2 = self.findroot(c2)
        if self.computers[root1] > self.computers[root2]:
            self.computers[root1] = root2
            self.computers[root2] -= 1
        else:
            self.computers[root2] = root1
            self.computers[root1] -= 1

    def check(self, c1, c2):
        if self.findroot(c1) == self.findroot(c2):
            print 'yes'
        else:
            print 'no'

    def netcheck(self):
        count = 0
        for computer in self.computers:
            if computer < 0:
                count += 1
        if count == 1:
            print 'The network is connected.'
        else:
            print 'There are {} components.'.format(count)


num = int(raw_input())
mynet = network(num)
while 1:
    userinput = raw_input()
    if userinput == 'S':
        break
    else:
        instr, c1, c2 = userinput.split()
        if instr == 'C':
            mynet.check(int(c1), int(c2))
        elif instr == 'I':
            mynet.union(int(c1), int(c2))

mynet.netcheck()




