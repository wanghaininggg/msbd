l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
l2 = list(set(l1))
l2.sort(key=l1.index) # 保持原来的顺序

l3 = sorted(set(l1), key=l1.index)

# for i in l1:
# #     if i not in l2:
# #         l2.append(i)

print(l2)
print(l3)