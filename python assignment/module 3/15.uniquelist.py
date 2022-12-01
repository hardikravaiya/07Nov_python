list=[1,4,5,6,6,7,3,8,9]
uniquelist= []

for a in list:
    if a not in uniquelist:
        uniquelist.append(a)

print(uniquelist)
