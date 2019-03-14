# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#
# Return: The protein string encoded by s.

# get the RNA strand to be transcribed
mrna_strand = input("Please enter the RNA strand to be translated: ")

# RNA codon table
rna_codon = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
             "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
             "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
             "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
             "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
             "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
             "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
             "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
             "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
             "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
             "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
             "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
             "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
             "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
             "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
             "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
             }

# initialize an array of codons
codons = []

# initialize a counter for our while oop
count = 0

# separate the mRNA strand into codons
while count < len(mrna_strand) - 3:
    codons.append(mrna_strand[count:count + 3])
    count += 3

# initialize an array of amino acids
amino_acids = []

# determine which codon corresponds to which amino acid
for i in codons:
    amino_acids.append(rna_codon[i])

# print the protein formed by the amino acids
print("".join(amino_acids))
