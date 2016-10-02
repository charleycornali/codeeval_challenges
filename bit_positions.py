# -*- coding: utf-8 -*-
"""
Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not. Positions p1 and p2 are 1 based.

INPUT SAMPLE:

The first argument will be a path to a filename containing a comma separated list of 3 integers, one list per line. E.g.

86,2,3
125,1,2

OUTPUT SAMPLE:

Print to stdout, 'true'(lowercase) if the bits are the same, else 'false'(lowercase). E.g.

true
false

"""

import sys


def main():
	file_objet = open(sys.argv[1], 'r')
	for line in file_objet.readlines():
		print 'true' if bits_in_same_position(line) else 'false'


def bits_in_same_position(line):
    n, p1, p2 = list(map(int, line.split(',')))
    bits = bin(n)[2:]
    if p1 > len(bits) or p2 > len(bits):
    	bits = '0' * (max(p1, p2) - len(bits)) + bits

    return bits[-p1] == bits[-p2]


if __name__ == '__main__':
    main()