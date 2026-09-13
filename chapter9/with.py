# f = open("file.txt")

# data = f.read()

# print(data)

# f.close()

# try this with with statement
with open("myfile.txt") as f:
    data = f.read()
    print(data)