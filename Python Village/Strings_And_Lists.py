# intends to split a string from a given .txt file by the integers a, b, c, and d on the following line separated
# by spaces from index a up to b (inclusive) and index c up to d (inclusive)

filename = input("Input file name... ")

data = open(filename, "r")

word = data.readlines(1)[0]

numbers = data.readlines(2)[0].split(" ")

a = int(numbers[0])
b = int(numbers[1]) + 1
c = int(numbers[2])
d = int(numbers[3]) + 1

print(word[a:b] + " " + word[c:d])
