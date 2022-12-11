def file_read(filename):
        with open (filename, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')