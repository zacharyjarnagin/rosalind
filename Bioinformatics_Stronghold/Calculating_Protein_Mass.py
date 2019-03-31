# Given: A protein string P of length at most 1000 aa.
#
# Return: The total weight of P. Consult the monoisotopic mass table.

# To represent the monoisotopic mass table
mass_table = {"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
              "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
              "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
              "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
              "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}

# Have the user input the protein string
protein_string = input("Input the protein string to be massed: ")

# Initialize the mass of the protein
protein_mass = 0

# Find the corresponding weight of each character in the mass_table and add it to protein_mass
for i in protein_string:
    protein_mass = protein_mass + mass_table[i]

# Print the protein_mass result to 3 decimals
print(round(protein_mass, 3))
