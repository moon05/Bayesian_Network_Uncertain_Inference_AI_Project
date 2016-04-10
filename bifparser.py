import os
import re

#replaces all the comments if any present
def replace_comments(line):
	return re.sub("\([\w\s,]+\)", "", line)

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
		
	vars_dict = {}
	defs_dict = {}
	
	foo = open(filename, "r")
	print "Name of file: " + filename
	print
	
	#variable loop
	while True:
		line = foo.readline()
		if line.startswith("probability"):
			break
			
		if line.startswith("variable"):
			name = re.sub("variable[\s]*", "", line.strip())
			name = re.sub("[\s]*\{", "", name)
			line = foo.readline()
			vals = re.sub("type[\s]*discrete[\s]*\[[\s]*[\d]+[\s]*\]", "", line.strip())
			vals = re.sub("[\{\};\s]+", "", vals)
			vals = vals.split(",")
			vars_dict[name] = vals
			foo.readline()
	
	#definitions loop
	while True:
		line = foo.readline()
		if line == "":
			break
		
		if line.startswith("probability"):
			map_entry = re.sub("probability[\s]*|\{", "", line.strip())
			map_entry = re.sub("[\(\)]+", "", map_entry).strip()
			defs_dict[map_entry] = []
			while "}" not in peek_line(foo):
				line = foo.readline()
				vals = replace_comments(line).strip()
				vals = vals.strip(";")
				vals = vals.split(",")
				defs_dict[map_entry].append(vals)
			foo.readline()
	return (vars_dict, defs_dict)