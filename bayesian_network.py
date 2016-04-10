import sys
import xmlparser

vars_dict = {}
defs_dict = {}

#creates a string of the definitions dictionary with elements separated by line
def defs_dict_tostring(entry):
	length = len(defs_dict[entry])
	string = ""
	for element in defs_dict[entry]:
		string += str(element) + "\n"
	return string

#prints variables dictionary
def print_vars():
	print "Variables Dictionary:"
	for entry in vars_dict:
		print("%s: %s" % (entry, vars_dict[entry]))
	print

#prints definitions dictionary
def print_defs():
	print "Definitions Dictionary:"
	for entry in defs_dict:
		print("P(%s):\n%s" % (entry, defs_dict_tostring(entry)))
	print
	
#main routine
if len(sys.argv) != 2:
	print "Usage: bayesian_network.py <filename>"
	exit(-1)
	
bn = xmlparser.parse(sys.argv[1])
vars_dict = bn[0]
defs_dict = bn[1]

print_vars()
print_defs()