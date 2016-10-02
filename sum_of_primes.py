"""
CHALLENGE DESCRIPTION:

Write a program which determines the sum of the first 1000 prime numbers.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the sum of the first 1000 prime numbers.
3682913

"""
import sys
from math import sqrt


def primes_sum(num_of_primes_to_sum=None):
	if num_of_primes_to_sum is None:
		num_of_primes_to_sum = 1000
	
	num = 0
	primes = []

	while len(primes) < num_of_primes_to_sum:
		if is_prime(num):
			primes.append(num)
		num += 1

	sys.stdout.write(str(sum(primes)))


def is_prime(num):
    prime = False

    if num > 1:
        prime = True
        k = 2
        n = sqrt(num)
        
        while k <= n and prime == True:
        
            if num % k == 0:
                prime = False
            k += 1

    return prime

if __name__ == '__main__':
    primes_sum(1000)