import sys
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
				map_entry = trim(line, "FOR")
				while "<GIVEN>" in peek(foo):
					given = trim(foo.readline(), "GIVEN")
					map_entry = map_entry + " " + given
				defs_dict[map_entry] = []
				if "<TABLE>" in peek(foo):
					line = foo.readline().replace("<TABLE>", "")
					while "</TABLE>" not in line:
						line = replace_comments(line).strip()
						if line != "":
							table = line.split()
							for i in range(len(table)):
								table[i] = float(table[i])
							defs_dict[map_entry].append(table)
						line = foo.readline()
					line = replace_comments(line).strip().replace("</TABLE>", "")
					if line != "":
						table = line.split()
						for i in range (len(table)):
							table[i] = float(table[i])
						defs_dict[map_entry].append(table)
	
	print "Variables Dictionary:"
	for entry in vars_dict:
		print("%s: %s" % (entry, vars_dict[entry]))
	print
	
	print "Definitions Dictionary:"
	for entry in defs_dict:
		print("%s: %s" % (entry, defs_dict[entry]))
	print
	
if len(sys.argv) != 2:
	print "Usage: xmlparser.py <filename>"
	exit(-1)

parser(sys.argv[1])
