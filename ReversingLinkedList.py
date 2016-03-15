class stack(object):

    "stack object"

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


InPut = """00100 6 5
00000 4 99999
00100 1 12309
68237 6 -1
54312 9 45321
12578 10 45631
33218 3 00000
99999 5 68237
12309 2 33218""".split('\n')

# InPut = """00100 2 5
# 00100 1 12309
# 12309 2 -1
# 68237 6 -1
# 54312 9 45321
# 12578 10 45631""".split('\n')


def RevSL(InPut):
    "reverse a single linked list"
    # get the information of the list from first line
    start = InPut[0].split()[0]
    num = int(InPut[0].split()[1])
    maxsize = int(InPut[0].split()[2])

    # print maxsize
    stackone = stack(maxsize)  # initialise the stack with a given maxsize
    data = {}  # initialise the index

    # use address as the keyword to create the index
    for i in range(1, len(InPut)):
        temp = InPut[i].split()
        data[temp[0]] = [temp[1], temp[2]]

    keyword = start
    res = []

    # start with the first element of the list and put everyone in the stack
    while True:

        # if the stack is not full ,push the element to it
        if not stackone.isfull():
            stackone.push(keyword)
            # if this is the last element , break the circle
            if data[keyword][1] == '-1':
                break
            else:
                # if not the last, find the next element
                keyword = data[keyword][1]
        else:  # when the stack is full, pop the element until it's empty
            while not stackone.isempty():
                temp = stackone.pop()

                if res == []:  # the frist element
                    res.append("%s %s" % (temp, data[temp][0]))
                else:
                    # give the last element the point of this one, so link them
                    res[-1] = res[-1] + ' ' + temp
                    res.append("%s %s" % (temp, data[temp][0]))

    while not stackone.isempty():  # take the rest element in the stack
        temp = stackone.pop()
        if res == []:  # the frist element
            res.append("%s %s" % (temp, data[temp][0]))
        else:
            res[-1] = res[-1] + ' ' + temp
            res.append("%s %s" % (temp, data[temp][0]))

    res[-1] = res[-1] + ' ' + '-1'  # give the last element a null next point

    return res


def ResSL_1(InPut):
    "reverse a single linked list"
    # get the information of the list from first line
    start = InPut[0].split()[0]
    num = int(InPut[0].split()[1])
    maxsize = int(InPut[0].split()[2])
    time_max = num / maxsize
    stackone = stack(maxsize)  # initialise the stack with a given maxsize
    data = {}  # initialise the index

    # use address as the keyword to create the index
    for i in range(1, len(InPut)):
        temp = InPut[i].split()
        data[temp[0]] = [temp[1], temp[2]]

    keyword = start
    res = []
    time_now = 0
    if time_max > 0:  # check if it's necesarry to go into the circle,
                      # if time_max == 0, then no element needs to be reverse
        while time_now < time_max:

            # if the stack is not full ,push the element to it
            if not stackone.isfull():
                stackone.push(keyword)
                # if not the last, find the next element
                keyword = data[keyword][1]
            else:  # when the stack is full, pop the element until it's empty
                while not stackone.isempty():
                    temp = stackone.pop()
                    if res == []:  # the frist element
                        res.append("%s %s" % (temp, data[temp][0]))
                    else:
                        # give the last element the point of this one, in order
                        # to link them
                        res[-1] = res[-1] + ' ' + temp
                        res.append("%s %s" % (temp, data[temp][0]))
                time_now += 1

        res[-1] = res[-1] + ' ' + keyword

    if time_max == 0 or num%maxsize != 0: #check if there is last element frome the circle.
        while True: #append the last element into the result
            res.append("%s %s %s" % (keyword, data[keyword][0], data[keyword][1]))
            if data[keyword][1] == '-1':
                break
            keyword = data[keyword][1]

    return res

print ResSL_1(InPut)
