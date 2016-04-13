vars_dict = {}
defs_dict = {}
	
#returns the probability of the query given a particular assignment
def P(var, e, index):
	vals = []
	par = parents(var)
	for element in e:
		if element in par:
			vals.append(e[element])
	return defs_dict[(var, par)][tuple(vals)][index]
	
#returns list of parents
def parents(query):
	for entry in defs_dict:
		if entry[0] == query:
			return entry[1]
	return ()
	
#returns a list of variables in sorted topological order
def topological_sort():
	vars = vars_dict.keys()
	order = []
	i = 0
	while i < len(vars):
		if not parents(vars[i]):
			order.append(vars[i])
			del vars[i]
		else:
			i += 1
	while vars:
		temp = []
		i = 0
		while i < len(vars):
			if parents(vars[i])[0] in order:
				temp.append(vars[i])
				del vars[i]
			else:
				i += 1
		for element in temp:
			order.append(element)
	return order
	
#creates string to represent probability
def entry_tostring(entry):
	length = len(entry[1])
	string = entry[0]
	if length > 0:
		string += " | " + entry[1][0]
		for i in range(1, length):
			string += ", " + entry[1][i]
	return string

#creates a string of the definitions dictionary with elements separated by line
def dict_tostring(dict, entry):
	length = len(dict[entry])
	string = ""
	for element in dict[entry]:
		string += str(element) + ": " + str(dict[entry][element]) + "\n"
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
	print_dist_dict(defs_dict)

#prints the distribution for a dictionary of probability
def print_dist_dict(dict):
	for entry in dict:
		print("P(%s):\n%s" % (entry_tostring(entry), dict_tostring(dict, entry)))