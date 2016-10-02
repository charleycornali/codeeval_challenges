# -*- coding: utf-8 -*-
"""
Write a program which reverses the words in an input sentence.

INPUT SAMPLE:

The first argument is a file that contains multiple sentences, one per line. Empty lines are also possible.

For example:

Hello World
Hello CodeEval

OUTPUT SAMPLE:

Print to stdout each sentence with the reversed words in it, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces in each line you print.

For example:

World Hello
CodeEval Hello

"""

import sys, re


def reverse_words(file_name):
	file_objet = open(file_name, 'r')
	inputs = map(lambda _: re.sub('\n', '', _), file_objet.readlines())

	for input_str in inputs:
		if input_str:
			sys.stdout.write(' '.join(input_str.split(' ')[::-1]) + '\n')


if __name__ == '__main__':
    reverse_words(sys.argv[1])