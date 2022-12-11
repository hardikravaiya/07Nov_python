with open(r"test.txt", 'r') as ab:
    lines = len(ab.readlines())
    print('Total Number of lines:', lines)