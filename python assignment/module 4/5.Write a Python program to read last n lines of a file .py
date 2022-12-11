def LastNlines(filename, a):
   
    with open(filename) as file:
        for line in (file.readlines() [-a:]):
            print(line, end ='')
if __name__ == '__main__':
    fname = 'test.txt'
    N = 3
    try:
        LastNlines(fname, N)
    except:
        print('File not found')