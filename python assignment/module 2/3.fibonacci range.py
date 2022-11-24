v=int(input("|enter your value: "))
a=0
b=1
sum=0
c=1
print("fibonacci series: ",end=" ")
while(c <= v):
    print(sum, end = " ")
    c+=1
    a=b
    b=sum
    sum=a+b
 