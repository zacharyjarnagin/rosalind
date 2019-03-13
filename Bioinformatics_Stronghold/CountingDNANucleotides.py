# intended to output the counts of each base in a given DNA strand

strand = input("Insert strand: ")

a = str(strand.count("A"))
c = str(strand.count("C"))
g = str(strand.count("G"))
t = str(strand.count("T"))

print(a + " " + c + " " + g + " " + t)
