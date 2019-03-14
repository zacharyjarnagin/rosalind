# Given: Positive integers n≤40 and k≤5.
#
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and
# in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs
# (instead of only 1 pair).

# below is my old solution, which had an awful runtime

# def rabbit_fib(n, k, age):
#     if n == 1 or n == 0:
#             return 1
#     elif age >= 1:
#         return rabbit_fib(n - 1, k, age + 1) + k * rabbit_fib(n - 1, k, 0)
#     else:
#         return rabbit_fib(n - 1, k, age + 1)
#

# below is an example solution from the Rosalind Project, which memorizes previous answers to save
# unnecessary recursive calls, thus leading to a much better runtime

# initialize an empty dictionary of previous or memorized answers

memo = {}


# fib is a function that takes in n for the nth term in the fibonacci sequence and how many times k we need to
# multiply the recursive call to represent offspring
def fib(n, k=1):
    args = (n, k)
    if args in memo:
        return memo[args]  # Aha! We have computed this before!

    # We haven't computed this before, so we do it now
    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = fib(n-1, k) + k * fib(n-2, k)
    memo[args] = ans  # don't forget to remember the result!
    return ans


# gather the months passed and offspring size from the user
num_months = int(input("Enter the amount of months that will pass: "))
offspring_size = int(input("Enter the amount of rabbit pairs each liter will consist of: "))

# print the result based on user input
print(fib(num_months, offspring_size))
