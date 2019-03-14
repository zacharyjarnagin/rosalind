# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: The Hamming distance dH(s,t).

# Obtain the two DNA strands to be compared
strand1 = input("Enter the first DNA strand: ")
strand2 = input("Enter the second DNA strand: ")

# initialize a count representing the differences between the two DNA strands
differences = 0

# initialize a counter for our while loop
i = 0

# iterate through both strands; if the characters vary at the current index, add one to the differences
while i < len(strand1):
    if strand1[i] != strand2[i]:
        differences += 1
    i += 1

# print the total differences between the two DNA strands
print(differences)
