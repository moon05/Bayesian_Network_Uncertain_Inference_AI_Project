import sys
import os
import bayesian_network as bn
import xmlparser
import bifparser
import exact_inference
import rejection_sampling

inference_algorithms = {
	"exact" : exact_inference,
	"rejection" : rejection_sampling
}

#returns a list version of a dictionary
def dict_to_list(dict):
	dict_list = []
	for key, value in dict.iteritems():
		dict_list.append(key + " = " + value)
	return dict_list

#main routine
argc = len(sys.argv)
if argc < 3:
	print "Usage: main.py <algorithm> <filename> <input>*"
	exit(-1)

option = sys.argv[1].strip("-")
if option not in inference_algorithms:
	print "Error: not a valid inference algorithm"
	print "Options: exact, rejection_sampling"
	exit(-1)

#determines which parser should be used based on the file extension
filename, file_ext = os.path.splitext(sys.argv[2])
if file_ext == ".xml":
	result = xmlparser.parse(filename + file_ext)
elif file_ext == ".bif":
	result = bifparser.parse(filename + file_ext)
else:
	print "Error: invalid extension for bayesian network file"
	exit(-1)

#error handling for files
if result == ({}, {}):
	print "Error: file not found"
	exit(-1)

#bayes net (bn)
bn.vars_dict = result[0]
bn.defs_dict = result[1]

bn.print_vars()
bn.print_defs()

#checks which algorithm was specified in order to parse and run the algorithm
algorithm = inference_algorithms[option]

#obtains distribution list and checks for errors
result = algorithm.parse(bn, sys.argv[3:])
if result is None:
	exit(-1)

e_list = dict_to_list(result[1])
distribution = {(result[0], tuple(e_list)) : {() : result[2]}}
bn.print_dist_dict(distribution)