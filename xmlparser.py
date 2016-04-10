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

#adds a input to the definitions dictionary
def add_to_defs(line, query, map_entry, vars_dict, defs_dict):
	num_values = len(vars_dict[query])
	if line != "":
		table = line.split()
		length = len(table)
		i = 0
		while i < length:
			new_table = []
			for j in range(num_values):
				new_table.append(float(table[i + j]))
			defs_dict[map_entry].append(new_table)
			i += num_values

#parses input from an xml file
def parse(filename):
	if not os.path.exists(filename):
		return ({}, {})

	vars_dict = {}
	defs_dict = {}
	
	foo = open(filename, "r")
	print "Name of file: " + filename
	print
	
	#variable loop
	while True:
		line = foo.readline()
		if "<DEFINITION>" in line:
			break
		
		if "<VARIABLE" in line:
			line = foo.readline()
			if "<NAME>" in line:
				name = trim(line, "NAME")
				vars_dict[name] = []
				while "<OUTCOME>" in peek_line(foo):
					outcome = trim(foo.readline(), "OUTCOME")
					vars_dict[name].append(outcome)
	
	#definition loop
	while True:
		line = foo.readline()
		if ("</BIF>" in line):
			break
		
		if "<DEFINITION>" in line:
			line = foo.readline()
			if "<FOR>" in line:
				query = trim(line, "FOR")
				map_entry = query
				if "<GIVEN>" in peek_line(foo):
					map_entry += " | "
					while "<GIVEN>" in peek_line(foo):
						line = foo.readline()
						given = trim(line, "GIVEN")
						map_entry = map_entry + given + ", "
					map_entry = map_entry[0:-2]
					defs_dict[map_entry] = []
					if "<TABLE>" in peek_line(foo):
						line = foo.readline().replace("<TABLE>", "")
						while "</TABLE>" not in line:
							line = replace_comments(line).strip()
							add_to_defs(line, query, map_entry, vars_dict, defs_dict)
							line = foo.readline()
						line = replace_comments(line).strip().replace("</TABLE>", "")
						add_to_defs(line, query, map_entry, vars_dict, defs_dict)
	return (vars_dict, defs_dict)