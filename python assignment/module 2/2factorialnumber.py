number=int(input("Enter the number: "))
factorial=1
if number>=1:
    for i in range(1,number+1):
        factorial=factorial*i
print("factorial is given number is: ",factorial)