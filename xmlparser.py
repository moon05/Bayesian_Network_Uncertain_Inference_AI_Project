import sys
import os
import re

vars_dict = {}
defs_dict = {}

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
def peek(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

#adds a input to the definitions dictionary
def add_to_defs(line, given, map_entry):
	num_values = len(vars_dict[given])
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
def parser(filename):
	foo = open(filename, "r")
	print "Name of file: " + filename

	#var loop
	while True:
		line = foo.readline()
		if ("<DEFINITION>" in line):
			break

		if "<VARIABLE" in line:
			line = foo.readline()
			if "<NAME>" in line:
				name = trim(line, "NAME")
				vars_dict[name] = []
				while "<OUTCOME>" in peek(foo):
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
				given = trim(line, "FOR")
				map_entry = given
				while "<GIVEN>" in peek(foo):
					given = trim(foo.readline(), "GIVEN")
					map_entry = map_entry + " " + given
				defs_dict[map_entry] = []
				if "<TABLE>" in peek(foo):
					line = foo.readline().replace("<TABLE>", "")
					while "</TABLE>" not in line:
						line = replace_comments(line).strip()
						add_to_defs(line, given, map_entry)
						line = foo.readline()
					line = replace_comments(line).strip().replace("</TABLE>", "")
					add_to_defs(line, given, map_entry)
	
	print "Variables Dictionary:"
	for entry in vars_dict:
		print("%s: %s" % (entry, vars_dict[entry]))
	print
	
	print "Definitions Dictionary:"
	for entry in defs_dict:
		print("%s: %s" % (entry, defs_dict[entry]))
	print

#main routine
if len(sys.argv) != 2:
	print "Usage: xmlparser.py <filename>"
	exit(-1)

if not os.path.exists(sys.argv[1]):
	print "Error: File not found"
	exit(-1)

parser(sys.argv[1])