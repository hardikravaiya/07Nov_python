my_dict= {'1':['p', 'y'], '2':['t', 'h']}
my_list= list(my_dict.values())
for a in my_list[0]:
    for b in my_list[1]:
        print(a+b)
