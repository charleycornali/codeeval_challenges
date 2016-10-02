# -*- coding: utf-8 -*-
"""
Write a program which reads a file and prints to stdout the specified number of the longest lines that are sorted based on their length in descending order.

INPUT SAMPLE:

Your program should accept a path to a file as its first argument. The file contains multiple lines. The first line indicates the number of lines you should output, the other lines are of different length and are presented randomly. You may assume that the input file is formatted correctly and the number in the first line is a valid positive integer.

For example:

2
Hello World
CodeEval
Quick Fox
A
San Francisco

OUTPUT SAMPLE:

Print out the longest lines limited by specified number and sorted by their length in descending order.

For example:

San Francisco
Hello World

"""
import sys, re

def main():
	file_object = open(sys.argv[1], 'r')
	lines = file_object.readlines()
	
	num_lines_to_print = int(re.sub('\n', '', lines[0]))
	word_length_dict = {}
	for idx, line in enumerate(lines):
		word_length_dict[len(re.sub('\n', '', line))] = line

	for _ in range(num_lines_to_print):
		key = max(word_length_dict.keys())
		sys.stdout.write(word_length_dict[key] + '\n')
		del word_length_dict[key]

if __name__ in '__main__':
	main()