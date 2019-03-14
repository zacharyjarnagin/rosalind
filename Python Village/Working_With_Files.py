# prints the even lines of a file

fileName = input("Input filename: ")

data = open(fileName, "r").readlines()

out = []

for i in range(len(data)):
    if i % 2 == 1:
        out.append(data[i])

for i in range(len(out)):
    print(out[i].rstrip())
