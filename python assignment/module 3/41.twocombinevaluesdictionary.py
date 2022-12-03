a = {'a': 12, 'for': 25, 'c': 9}
b = {'Geeks': 100, 'geek': 200, 'for': 300}
 
c = {i: a.get(i, 0) + b.get(i, 0)
     for i in set(a).union(b)}
print(c)
