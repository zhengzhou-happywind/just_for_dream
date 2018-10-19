#  给一个列表A，再给一个列表B，B中是A的索引，在循环中删除B
def del_index(l, index_l):
    a = 0
    for j in index_l:
        del l[j - a]
        a += 1
    return l


l1 = [1, 2, 3, 4, 5]
l2 = [0, 2, 3]
obj = del_index(l1, l2)
print(obj)
'''
[2, 5]
'''


'''
给一个列表去重，多种方法
l = ['b','c','d','b','c','a','a']

ll = list(set(l))
print(ll)

ll = []
[ll.append(i) for i in l if i not in ll]
print(ll)

ll = {}.fromkeys(l).keys()
print(ll)

ll = sorted(set(l), key=l.index)
print(ll)  # 这样就保持了原列表的排序方式，在sorted里面把原列表的索引作为sorted里面的key的参数
'''
