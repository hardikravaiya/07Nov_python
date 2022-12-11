n = int(input("Enter Lines To Read : "))
f = open("tested.txt","r")
for i in range(n):
	print(f.readline())
