def CheckSeq(lst, size):
    ''' take a lst, check if it's possible path for search tree'''
    min = 1 #set the bottom edge 
    max = size + 1 # set the top edge
    temp = lst[0] 
    for i in lst[1:]:
        if i not in range(min, max):
            #if the node is out of the range 
            return "NO"
        else:
            if i > temp:
                #the follow node is bigger
                min = temp #update bottom
            elif i < temp:
                #the follow node is smaller, update top
                max = temp + 1
            else: #cannot be the same
                return "NO"
            temp = i #update last node
    else: #if all the node is in the range
        return 'YES'

SeqNum, Size = [int(x) for x in raw_input().split()]
for x in range(SeqNum):
	lst = [int(y) for y in raw_input().split()]
	print CheckSeq(lst, Size)