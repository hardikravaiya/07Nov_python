a={'jay':43,'harsh':3,'hat':1,'vinod':3}                        
b=list(a.items())
b.sort()
print('Ascending order is: ',b) 
b=list(a.items())
b.sort(reverse=True) 
print('Descending order is: ',b)
dict=dict(b)
print("Dictionary: ",dict)