import sys
import os
import bayesian_network as bn
import xmlparser
import bifparser
import exact_inference

#returns a list version of a dictionary
def dict_to_list(dict):
	dict_list = []
	for key, value in dict.iteritems():
		dict_list.append(key + " = " + value)
	return dict_list

#main routine
argc = len(sys.argv)
if argc < 3 or argc % 2 == 0:
	print "Usage: main.py <filename> <query> [<given> <assignment>]*"
	exit(-1)

#determines which parser should be used based on the file extension
filename, file_ext = os.path.splitext(sys.argv[1])
if file_ext == ".xml":
	result = xmlparser.parse(filename + file_ext)
elif file_ext == ".bif":
	result = bifparser.parse(filename + file_ext)
else:
	print "Error: Invalid extension for bayesian network file"
	exit(-1)

#error handling for files
if result == ({}, {}):
	print "Error: File not found"
	exit(-1)
	
#bayes net (bn)
bn.vars_dict = result[0]
bn.defs_dict = result[1]

bn.print_vars()
bn.print_defs()

#obtains a distribution list and converts it into a map for output
query = sys.argv[2]
e = {}
i = 3
while i < argc:
	e[sys.argv[i]] = sys.argv[i+1]
	i += 2
result = exact_inference.enumeration_ask(query, e, bn)
e_list = dict_to_list(e)
distribution = {(query, tuple(e_list)) : {() : result}}
bn.print_dist_dict(distribution)