lst = []

num = int(input('How many numbers: '))

sum=int()
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
    sum=sum+numbers

print("Maximum element :", max(lst), "\nMinimum element :", min(lst))
print(sum)
