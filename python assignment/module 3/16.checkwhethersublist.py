list=['a','b',[1,3,4,5,'hello python']]

for a in list:
    if len (a)>1:
        print("sublist is present in list")
        break

else:
    print("sublist is not present in list")
