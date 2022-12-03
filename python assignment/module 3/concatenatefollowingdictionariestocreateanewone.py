a={1:1,2:2}
b={3:3,4:4}
c={5:5,6:6}
d={}
for h in (a, b, c): d.update(h)
print(d)