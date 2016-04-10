import sys
import os
import bayesian_network as bn
import xmlparser
import bifparser

#main routine
if len(sys.argv) != 2:
	print "Usage: main.py <filename>"
	exit(-1)

filename, file_ext = os.path.splitext(sys.argv[1])
if file_ext == ".xml":
	result = xmlparser.parse(filename + file_ext)
elif file_ext == ".bif":
	result = bifparser.parse(filename + file_ext)
else:
	print "Error: Invalid extension for bayesian network file"
	exit(-1)

if result == ({}, {}):
	print "Error: File not found"
	exit(-1)
	
bn.vars_dict = result[0]
bn.defs_dict = result[1]

bn.print_vars()
bn.print_defs()