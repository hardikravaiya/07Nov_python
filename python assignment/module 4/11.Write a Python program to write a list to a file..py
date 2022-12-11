names = []
with open(r'tested.txt', 'r') as fp:
    for line in fp:
        x = line[:-1]
        names.append(x)

print(names)