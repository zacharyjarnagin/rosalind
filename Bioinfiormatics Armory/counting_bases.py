# Given: A DNA string s of length at most 1000 bp.
#
# Return: Four integers (separated by spaces) representing the respective number of times that the symbols
# 'A', 'C', 'G', and 'T' occur in s.


class CountDNA:
    def __init__(self, strand):
        a = 0
        c = 0
        g = 0
        t = 0
        for char in strand:
            if char == 'A':
                a += 1
            elif char == 'C':
                c += 1
            elif char == 'G':
                g += 1
            elif char == 'T':
                t += 1
        self.strand = strand
        self.a = a
        self.c = c
        self.g = g
        self.t = t


strand = input("Enter the DNA strand: ")
dna = CountDNA(strand)
print("{} {} {} {}".format(dna.a, dna.c, dna.g, dna.t))
