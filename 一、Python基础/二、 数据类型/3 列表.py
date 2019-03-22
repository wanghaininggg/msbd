name_list = ["zhangsan", "lisi", "wangwu", "zhaoliu"]

# (1)增加 列表名.insert(index, 数据) 在指定的位置插入数据
name_list.insert(0, "Sasuke")
print(name_list)
name_list.insert(10, "Tome")  # 如果我们要在下标是6的地方插入数据，那个会自动插入到下标为5的地方，也就是插入到最后
print(name_list)
name_list.append("Python")
print(name_list)

# 列表.extend(Iterable): 将可迭代对象中的元素追加到列表

a = [11, 22, 33]
b = [44, 55, 66]
a.extend(b)
print(a)

c = ['j', 'a', 'v', 'a']  # 有列表c和字符串d c.extend(d)会将字符串拆开作为元素插入到列表c
d = 'python'
c.extend(d)
print(c)

# （2）取值和修改
name_list = ["zhangsan", 'lishi', 'wangwu', 'zhaoliu']
print(name_list[0])
name_list[0] = "Sasuke"
print(name_list)

# (3) 删除
name_list = ["zhangsan", "lisi", "wangwu", "zhaoliu", "dsafd", "sfdsfd"]
del name_list[0]
print(name_list)
name_list.remove('lisi')
print(name_list)
s = name_list.pop()  # 删除末尾的值；返回被删除的元素
s = name_list.pop(1)
name_list = ["zhangsan", "lisi", "wangwu", "zhaoliu"]
name_list.clear()
print(name_list)

# (4) 排序
a = [33, 44, 22, 66, 11]
print(a)
print(a.sort())

# (5) 统计相关
print(len(a))
print(a.count(11))
print(a.index(66))
print(11 in a)

# (6) 循环遍历
a = [11, 22, 33, 44, 55]

i = 0
while i < len(a):
    print(a[i])
    i += 1
for i in a:
    print(i)