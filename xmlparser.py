import os
import re

#replaces all the comments if any present
def replace_comments(line):
	return re.sub("<!--[\w\s!]+-->", "", line)

#trims the tags
def trim(line, delim):
	line = line.strip()
	line = replace_comments(line)
	left = "<" + delim + ">"
	right = "</" + delim + ">"
	line = line.replace(left, "").replace(right, "")
	return line
	
#looks at the upcoming line instead of actually reading it
def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

#generates tuple of the assignments of the current map_entry being added
def get_current_assignment(map_entry, size, vars_list_dict):
	assignment = []
	length = len(map_entry[1])
	for i in range(length):
		pow = 2**(length-i-1)
		num_values = len(vars_list_dict[map_entry[1][i]])
		assignment.append(vars_list_dict[map_entry[1][i]][size/pow % (num_values)])
	return tuple(assignment)

#adds a input to the definitions dictionary
def add_to_defs(line, query, map_entry, vars_list_dict, defs_dict):
	num_values = len(vars_list_dict[query])
	if line != "":
		table = line.split()
		length = len(table)
		i = 0
		while i < length:
			new_table = []
			for j in range(num_values):
				new_table.append(float(table[i + j]))
			size = len(defs_dict[map_entry])
			assignment = get_current_assignment(map_entry, size, vars_list_dict)
			defs_dict[map_entry][assignment] = new_table
			i += num_values

#parses input from an xml file
def parse(filename):
	if not os.path.exists(filename):
		return ({}, {})

	vars_list_dict = {}
	defs_dict = {}
	
	foo = open(filename, "r")
	print "Name of file: " + filename
	print
	
	#variable loop
	while True:
		if "<DEFINITION>" in peek_line(foo):
			break
		
		line = foo.readline()
		if "<VARIABLE" in line:
			line = foo.readline()
			if "<NAME>" in line:
				name = trim(line, "NAME")
				vars_list_dict[name] = []
				while "<OUTCOME>" in peek_line(foo):
					outcome = trim(foo.readline(), "OUTCOME")
					vars_list_dict[name].append(outcome)
	
	#definition loop
	while True:
		if "</BIF>" in peek_line(foo):
			break
		
		line = foo.readline()
		if "<DEFINITION>" in line:
			line = foo.readline()
			if "<FOR>" in line:
				query = trim(line, "FOR")
				map_entry = [query, []]
				if "<GIVEN>" in peek_line(foo):
					while "<GIVEN>" in peek_line(foo):
						line = foo.readline()
						given = trim(line, "GIVEN")
						map_entry[1].append(given)
				map_entry[1] = tuple(map_entry[1])
				map_entry = tuple(map_entry)
				defs_dict[map_entry] = {}
				if "<TABLE>" in peek_line(foo):
					line = foo.readline().replace("<TABLE>", "")
					while "</TABLE>" not in line:
						line = replace_comments(line).strip()
						add_to_defs(line, query, map_entry, vars_list_dict, defs_dict)
						line = foo.readline()
					line = replace_comments(line).strip().replace("</TABLE>", "")
					add_to_defs(line, query, map_entry, vars_list_dict, defs_dict)
	foo.close()
	return (vars_list_dict, defs_dict)