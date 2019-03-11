# 在Python中用于生成随机数的模块式random，在使用前需要import

import random
a = 1
b = 10
print(random.random())  # 生成一个0-1之间的随机浮点数
print(random.uniform(a, b))  # 生成[a, b]之间的浮点数
print(random.randint(a, b))  # 生成[a, b]之间的整数
print(random.randrange(a, b, step=2))  # 在指定的集合[a, b)中，以step为基数随机取一个数;
random.choice([1, 2, 3, 4, 5])  # 在特定的序列中随机取一个元素，这里的序列可以是字符串，列表，元祖等；
