# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single
# solution.)


# get the file that holds the information we want
filename = input("Enter the name of the .txt file in FASTA format: ")

# read the .txt file
with open(filename, "r") as f:
    data = f.read()
f.close()

# clean the string and place each strand in an array
for line in data.split("\n"):
    if line.startswith(">"):
        data = data.replace(line, ">")
data = data.replace("\n", "")
data = data.split(">")[1:]


# the main function
def find_motif():
    # start with the smallest string
    string = min(data, key=len)
    i = 0
    possible_motifs = []
    while i < len(string):
        distance = len(string)
        while distance > 2 & i + distance <= len(string):
            does_exist = True
            for strand in data:
                if string[i:i + distance] not in strand:
                    does_exist = False
                    break
            if does_exist:
                possible_motifs.append(string[i:i + distance])
            distance -= 1
        i += 1
    # return the longest common motif of our strands
    return max(possible_motifs, key=len)


# print the longests strand
print(find_motif())
