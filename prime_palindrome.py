# -*- coding: utf-8 -*-
"""
Write a program which determines the largest prime palindrome less than 1000.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the largest prime palindrome less than 1000.
929
"""

import sys
from math import sqrt


def find_largest_prime_palindrome(n=None):
	if n is None:
		n = 1000

	largest_prime_palindrome = None

	for num in range(n, 1, -1):

		if is_prime(num):
			if is_palindrome(num) and num % 11 != 0:
				largest_prime_palindrome = num
				break
	
	sys.stdout.write(str(largest_prime_palindrome))


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


def is_palindrome(num):
	return str(num) == str(num)[::-1]


if __name__ == '__main__':
    find_largest_prime_palindrome(1000)