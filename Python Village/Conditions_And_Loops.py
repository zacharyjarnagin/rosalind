# intends to print out the sum of all odd numbers from a to b within a given .txt file separated by spaces

fileName = input("Input filename: ")

data = open(fileName, "r").readlines()[0].split(" ")


a = int(data[0])
b = int(data[1])

sum = 0

if a % 2 == 0:
    a += 1

while a < b:
    sum += a
    a += 2

print(sum)
