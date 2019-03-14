# Given: Two DNA strings s and t (each of length at most 1 kbp).
#
# Return: All locations of t as a substring of s.

# obtain the DNA strand to be analyzed and the motif we wish to find
dna_strand = input("Enter DNA strand to be analyzed: ")
motif = input("Enter motif to be found: ")

# initialize a list of locations where the motif is found
locations = []

# initialize two variable for looping
i = 0
motif_length = len(motif)

# loop through the DNA strand and append the string location of the motif in the strand if it is found
while i + motif_length <= len(dna_strand):
    if dna_strand[i:i + motif_length] == motif:
        locations.append(str(i + 1))
    i += 1

# convert the locations list into a string
locations_output = " ".join(locations)

# print the locations where the motif was found
print(locations_output)
