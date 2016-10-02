# -*- coding: utf-8 -*-
"""
CHALLENGE DESCRIPTION:

By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

   5
  9 6
 4 6 8
0 7 1 5
5 + 9 + 6 + 7 = 27

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following:

5
9 6
4 6 8
0 7 1 5
You make also check full input file which will be used for your code evaluation.

OUTPUT SAMPLE:

The correct output is the maximum sum for the triangle. So for the given example the correct answer would be

27
"""

import re, sys

def main():
    file_objet = open(sys.argv[1], 'r')
    lines = file_objet.readlines()
    print lines
    sys.stdout.write(str(get_sum_of_triangle_numbers(lines)))

def get_sum_of_triangle_numbers(lines):
    triangle_sum = 0

    for idx, line in enumerate(lines):
        if not line:
            continue
            
        values = re.sub('\n', '', line).split(' ')
        if idx < 2:
            idx_to_add = 0
        else:
            idx_to_add = 1
        triangle_sum += int(values[idx_to_add])
    return triangle_sum


if __name__ == '__main__':
    main()