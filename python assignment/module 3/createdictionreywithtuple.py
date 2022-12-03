def Convert(tup, di):
    di = dict(tup)
    return di
      

abcd = [("hardik", 1), ("gaurav", 2), ("jay", 3),  ("tejash", 4), ("dhaval", 5), ("sanket", 6)]
dictionary = {}
print (Convert(abcd, dictionary))
print(abcd['hardik'])
print(abcd['gaurav'])
print(abcd['jay'])
print(abcd['tejash'])
print(abcd['sanket'])