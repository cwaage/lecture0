#!/usr/bin/env python3

import sys

num_args = len(sys.argv)

if num_args > 2:

	file_name = sys.argv[1]
	text = sys.argv[2]

else:
	
	print("Usage: file_op.py <file_name> <message>")
	sys.exit()

outFile = open(file_name, "w")
outFile.write(text)


