a=[1,2,3,4,5,6,7]
b=[2,5,6,7,8,9,4]

c=[]

for number in a:
    if number in b:
        if number not in c:
            c.append(number)

print(c)
