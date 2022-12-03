a={}

b=int(input("number your elements:"))

for i in range(b):
    c=input("enter key:")
    d=input("enter value:")
    a.update({c:d})

print(a)

f={}
e=int(input("number your elements:"))

for l in range(e):
    m=input("enter key:")
    n=input("enter value:")
    f.update({m:n})

print(f)

o=a.copy()
o.update(f)
print(o)