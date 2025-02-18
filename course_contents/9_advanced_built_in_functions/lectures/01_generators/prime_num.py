"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""

# 2 will never enter the loop
def prime_generator(bound):
    for n in range(2, bound):   # n starts from 2 to bound
        for x in range(2, n):   # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:   # if no such x is found after exhausting all 1<x<n
            yield n     # generate this prime

prime_nums = prime_generator(100)
print(next(prime_nums))
print(next(prime_nums))

print(list(prime_nums))

