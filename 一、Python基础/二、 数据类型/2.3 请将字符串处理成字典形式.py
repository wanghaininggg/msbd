str1 = 'k:1|k1:2|k2:3|k3:4'

a = str1.split('|')
d = {}
for i in a:
    k, y = i.split(':')
    d[k] = y

print(d)
print({key: value for (key, value) in [x.split(':') for x in str1.split('|')]})
