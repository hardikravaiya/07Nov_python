def file_read(filename):
        from itertools import islice
        with open(filename, "w") as myfile:
                myfile.write("Python program\n")
                myfile.write("Java program\n")
                myfile.write("c++ program")
        txt = open(filename)
        print(txt.read())
file_read('tested.txt')
