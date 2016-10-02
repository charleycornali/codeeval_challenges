# -*- coding: utf-8 -*-
"""
Given numbers x and n, where n is a power of 2, print out the smallest multiple of n which is greater than or equal to x. Do not use division or modulo operator.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated list of two integers, one list per line. E.g.

13,8
17,16

OUTPUT SAMPLE:

Print to stdout, the smallest multiple of n which is greater than or equal to x, one per line. E.g.

16
32

"""

import sys, re


def main():
	file_objet = open(sys.argv[1], 'r')
	for line in file_objet.readlines():
		multiples_of_num(re.sub('\n', '', line))


def multiples_of_num(file_line):
	threshold, num = map(int, file_line.split(','))
	tester_num = 1
	
	while True:
		if threshold <= num * tester_num:
			print num * tester_num
			break
		tester_num += 1


if __name__ == '__main__':
    main()