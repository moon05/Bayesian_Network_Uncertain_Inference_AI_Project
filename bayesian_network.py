vars_dict = {}
defs_dict = {}
	
#returns the probability of the query given a particular assignment
def P(var, val):
	index = -1
	for i in range(len(vars_dict[Y])):
		if val == vars_dict[Y][i]:
			index = i
			break
	return None

#returns list of parents
def parents(query):
	for entry in defs_dict:
		if entry[0] == query:
			return entry[1]
	return None

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
		print("P(%s):\n%s" % (entry_tostring(entry), defs_dict_tostring(entry)))
	print