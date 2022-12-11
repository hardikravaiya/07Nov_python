import random
file = open ("hardik.txt","w")
file.write('''hello everyone
this is python basic programing course
and very easy this program 
''')
file.close ()
read = open ("hardik.txt","r")
lines = read.readlines()
a = 0
print ("All lines of file :-\n")
for i in lines :
    print (f"{a} : {i}")
    a += 1

x = random.choice(lines)

print (f"Random line form file is :- \n{x}")

read.close()
