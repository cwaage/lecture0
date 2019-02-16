#!/usr/bin/env python3

import sys

num_args = len(sys.argv)

if num_args > 1:

	file_name = sys.argv[1]

else:
	
	print("Usage: file_op.py <file_name>")
	sys.exit()

outFile = open(file_name, "w")


