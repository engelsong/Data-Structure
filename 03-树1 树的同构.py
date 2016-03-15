

def TreeCheck(tree1, tree2):
    res = True
    keys1 = sorted(tree1.keys())
    keys2 = sorted(tree2.keys())
    if keys1 != keys2:
        res = False
    else:
        for i in keys1:
            if tree1[i] != tree2[i] and tree1[i] != tree2[i][::-1]:
                res = False
    return res


def getNode(x, lst):
    res = None
    if x != '-':
        temp = int(x)
        res = lst[temp][0]
    return res


lst1 = []
lst2 = []
tree1 = {}
tree2 = {}

tree1_NodeNum = int(raw_input())
for time in range(tree1_NodeNum):
	lst1.append(raw_input().split())

tree2_NodeNum = int(raw_input())
for time in range(tree2_NodeNum):
	lst2.append(raw_input().split())

for i in lst1:
    tree1[i[0]] = [
        getNode(i[1], lst1), getNode(i[2], lst1)]

for i in lst2:
    # i = i.split()
    tree2[i[0]] = [
        getNode(i[1], lst2), getNode(i[2], lst2)]

if TreeCheck(tree1, tree2):
	print 'Yes'
else:
	print 'No'