list = [] 
n = int(input("Enter the number of elements: "))
for a in range(1, n+1): 
    elem = int(input("Enter the elements: ")) 
    list.append(elem) 
list.sort() 

print("The sorted list: ", list) 
print("The second smallest value of this list: ",list[1])