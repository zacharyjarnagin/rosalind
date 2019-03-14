# intended to print out the given DNA strand in terms of RNA molecules by replacing T's with U's

dna = input("Please enter the DNA strand: ")

rna = ""

for i in dna:
    if i == "T":
        rna = rna + "U"
    else:
        rna = rna + i

print(rna)
