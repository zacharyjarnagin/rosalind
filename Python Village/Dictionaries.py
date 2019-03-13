# prints the unique words and the amount of times that word appears in a sentence that appears in a .txt file

fileName = input("Input filename: ")

data = open(fileName, "r").readlines()[0].strip().split(" ")

d = {}

for i in range(len(data)):
    d[data[i]] = 0

for i in range(len(data)):
    if data[i] in d:
        d[data[i]] += 1

for key, value in d.items():
    print(key + " " + str(value))
