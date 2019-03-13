# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a
# dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

hd = int(input("Enter # of homozygous dominant individuals: "))  # hd = homozygous dominant
he = int(input("Enter # of heterozygous individuals: "))  # he = heterozygous
hr = int(input("Enter # of homozygous recessive individuals: "))  # hr = homozygous recessive

# calculate total population
pop = hd + he + hr

# hd branch of probability tree
hd_hd = (hd / pop) * ((hd - 1) / (pop - 1))
hd_he = (hd / pop) * (he / (pop - 1))
hd_hr = (hd / pop) * (hr / (pop - 1))

# he branch of probability tree
he_he = (he / pop) * ((he - 1) / (pop - 1))
he_hd = (he / pop) * (hd / (pop - 1))
he_hr = (he / pop) * (hr / (pop - 1))

# hr branch of probability tree
hr_hr = (hr / pop) * ((hr - 1) / (pop - 1))
hr_hd = (hr / pop) * (hd / (pop - 1))
hr_he = (hr / pop) * (he / (pop - 1))

# add up probabilities where mating organisms produce 4/4 possible dominant offspring
prob_all_dom = hd_hd + hd_he + hd_hr + he_hd + hr_hd

# add up probabilities where mating organisms produce 3/4 dominant offspring (he * he)
# and 2/4 dominant offspring (he * hr)
prob_partial_dom = ((3 / 4) * he_he) + ((2 / 4) * hr_he) + ((2 / 4) * he_hr)

# print the sum of the above probabilities to get the probability of producing a dominant offspring
print(prob_all_dom + prob_partial_dom)
