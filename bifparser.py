import os
import re

#generates a tuple of the assignments by reading the in line comments
def get_current_assignment(line):
	string = re.sub("([\d]+(\.[\d]+)?,[\s]*)+[\d]+(\.[\d]+)?;", "", line).strip()
	if re.match("\(([\w]+,[\s]*)*[\w]+\)", string) is None:
		return tuple([])
	string = re.sub("[\s]+", "", string.lstrip("(").rstrip(")"))
	return tuple(string.split(","))

#replaces all the comments if any present
def replace_comments(line):
	return re.sub("\(([\w]+,[\s]*)*[\w]+\)", "", line)

#looks at the upcoming line instead of actually reading it
def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

#parses input from an bif file
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
		if peek_line(foo).startswith("probability"):
			break
		
		line = foo.readline()
		if line.startswith("variable"):
			name = re.sub("variable[\s]*", "", line.strip())
			name = re.sub("[\s]*\{", "", name)
			line = foo.readline()
			vals = re.sub("type[\s]*discrete[\s]*\[[\s]*[\d]+[\s]*\]", "", line.strip())
			vals = re.sub("[\{\};\s]+", "", vals)
			vals = vals.split(",")
			vars_list_dict[name] = vals
			foo.readline()
	
	#definitions loop
	while True:
		if peek_line(foo) == "":
			break
		
		line = foo.readline()
		if line.startswith("probability"):
			map_entry = re.sub("probability[\s]*|\{", "", line.strip())
			map_entry = re.sub("[\(\)]+", "", map_entry).strip()
			map_entry = re.sub("[\s\|,]+", ",", map_entry).split(",")
			map_entry = [map_entry[0], map_entry[1:]]
			map_entry[1] = tuple(map_entry[1])
			map_entry = tuple(map_entry)
			defs_dict[map_entry] = {}
			while "}" not in peek_line(foo):
				line = foo.readline()
				assignment = get_current_assignment(line);
				vals = replace_comments(line).strip()
				vals = re.sub("table", "", vals).strip()
				vals = vals.strip(";")
				vals = vals.split(",")
				for i in range(len(vals)):
					vals[i] = float(vals[i])
				defs_dict[map_entry][assignment] = vals
			foo.readline()
	foo.close()
	return (vars_list_dict, defs_dict)