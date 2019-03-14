# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated

# get the file that holds the information we want
filename = input("Enter the name of the .txt file in FASTA format: ")

# read the .txt file
with open(filename, "r") as f:
    data = f.read()
f.close()

# Get rid of line breaks and split the string into a list of strings containing the string ID and DNA strand
data = data.replace('\n', '').split('>')[1:]

gc_contents = []

# calculate the GC-content of each DNA strand
for i in data:
    gc_content = (i[13:].count('G') + i[13:].count('C')) / len(i[13:])
    gc_contents.append(gc_content * 100)

# determine the DNA strand with the highest GC-content
highest_gc_content = max(gc_contents)

# get the id of the DNA strand with the highest GC-content
highest_gc_id = data[gc_contents.index(highest_gc_content)][:13]

# print both the ID and GC-content of the DNA strand with the highest GC-content
print(highest_gc_id + "\n" + str(highest_gc_content))
