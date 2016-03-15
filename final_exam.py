
def solve(lst_post, lst_in, lenth):
    queue = []
    res = []
    lst_post = lst_post[::-1]
    root = lst_post.pop(0)
    res.append(root)
    index = lst_in.index(root)
    queue.append(lst_in[:index])
    queue.append(lst_in[index + 1:])
    while len(queue) != 0:
        temp = queue.pop(0)
        print temp
        if len(temp) == 1:
            res.append(temp[0])
        else:
            for i in lst_post:
                if i in temp:
                    res.append(i)
                    lst_post.remove(i)
                    index = temp.index(i)
                    queue.insert(0, temp[index + 1:])
                    queue.insert(0, temp[:index])
                    break
    return res



lenth = int(raw_input())
lst_post = map(int, raw_input().split())
lst_in = map(int, raw_input().split())
lst_pre = solve(lst_post, lst_in, lenth)
ans = ''
for i in range(lenth):
    ans += ' '+str(i)
print 'Preorder:' + ans