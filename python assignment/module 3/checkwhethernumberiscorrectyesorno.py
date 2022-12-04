ab=int(input("Enter the number: "))  

bc=0  

for c in range(1,ab):  
    if(ab % c==0):  
        bc=bc+c  
if(bc==ab):  
    print("The entered your number is correct")  
else:  
    print("The entered your number is incorrent")  