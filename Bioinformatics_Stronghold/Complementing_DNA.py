# intended to print out the reverse complement of a given DNA strand

dna = input("Please enter the DNA strand: ")

comp = ""

for i in dna:
    if i == "A":
        comp = "T" + comp
    elif i == "T":
        comp = "A" + comp
    elif i == "G":
        comp = "C" + comp
    else:
        comp = "G" + comp

print(comp)
