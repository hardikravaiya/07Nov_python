prompt = int(input("Enter an interger: "))
s=0
print("The divisors of the integer you entered are: ")

for i in range(1, prompt+1):
    if(prompt%i==0):
        s += i
        print(i)
print ("The sum of the divisors is: %d" %s)