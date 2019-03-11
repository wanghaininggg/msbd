l = []
for i in range(10):
    l.append({'num': i})
print(l)

l = []
a = {'num': 0}
for x in range(10):
    a['num'] = i
    l.append(a)
print(l)
# 字典是可变对象，在下方的l.append(a)的操作中把字典a的引用传到列表l中，
# 当后续操作修改a['num']的值的时候，l中的值也会跟着改变，相当于浅拷贝。
