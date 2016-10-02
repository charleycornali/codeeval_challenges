# -*- coding: utf-8 -*-
"""
Given a string write a program to convert it into lowercase.

INPUT SAMPLE:

The first argument will be a path to a filename containing sentences, one per line. You can assume all characters are from the english language. E.g.

HELLO CODEEVAL
This is some text

OUTPUT SAMPLE:

Print to stdout, the lowercase version of the sentence, each on a new line. E.g.

hello codeeval
this is some text

"""

import sys, re

def convert_sentance_to_lower(line):
    return re.sub('\n', '', line).lower()

def main():
    file_object = open(sys.argv[1], 'r')
    for line in file_object.readlines():
        sys.stdout.write(convert_sentance_to_lower(line) + '\n')


if __name__ == '__main__':
    main()
    