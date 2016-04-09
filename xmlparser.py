<<<<<<< HEAD
import sys
import os
import re

vars_dict = {}
defs_dict = {}
=======
import os
import re

variablesDict = {}
ListDefinitions = {}
maxVarNum = 0

# [{'A':[[.011,.99]]}, {'B':[[1223,123213]]}, {(A|B,E):[[0.95 ,0.05],[0.94,0.06],[0.29 ,0.71],[0.001,0.999]]}]
#
>>>>>>> 18f5f8edf1b26e8df2db3ae770c02ac919b92a8e

#to find out whats the maximum number of values any variable has
def maxTracker(varDict):
	global maxVarNum
	for n in varDict:
		if len(varDict[n]) > maxVarNum:
			maxVarNum = len(varDict[n])

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

<<<<<<< HEAD
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
=======
		if "<!-- Variables -->" in line:
			continue

		if "<VARIABLE" in line:
			continue

		if "<NAME>" in line:
			print "Collecting variable names"
			name = trim(line, "NAME")
			print name
			variablesDict[name] = []
			while "<OUTCOME>" in peek(foo):
				# print "Collecting values"
				outcome = trim(foo.readline(), "OUTCOME")
				# print outcome
				variablesDict[name].append(outcome)
			print variablesDict[name]
		if "<DEFINITION" in line:
			continue

		#calculating maxVarNum
		maxTracker(variablesDict)

		if "<FOR>" in line:
			# print "Collecting table"
			map_entry = trim(line, "FOR")
			# print map_entry
			
			if "<GIVEN>" in peek(foo):
>>>>>>> 18f5f8edf1b26e8df2db3ae770c02ac919b92a8e
				while "<GIVEN>" in peek(foo):
					line = foo.readline()
					given = trim(line, "GIVEN")
					map_entry = map_entry + " " + given
<<<<<<< HEAD
				defs_dict[map_entry] = []
				if "<TABLE>" in peek(foo):
					line = foo.readline().replace("<TABLE>", "")
					while "</TABLE>" not in line:
						line = replace_comments(line).strip()
						add_to_defs(line, given, map_entry)
						line = foo.readline()
					line = replace_comments(line).strip().replace("</TABLE>", "")
					add_to_defs(line, given, map_entry)
=======
				#map_entry has been updated
				print map_entry
				if "<TABLE>" and "</TABLE>" in peek(foo):
					print "inside both"
					line = foo.readline()
					ListDefinitions[map_entry] = list()
					table = trim(line, "TABLE")
					table = table.split()
					print table
					ListDefinitions[map_entry] = list()
					for n in range(len(table)):
						table[n] = float(table[n])
					for n in range(0,len(table),maxVarNum):
						ListDefinitions[map_entry].append(table[n:n+maxVarNum])
				
				elif "<TABLE>" in peek(foo):
					print "inside table"
					line = foo.readline()
					ListDefinitions[map_entry] = list()
					while "</TABLE>" not in peek(foo):
						line = foo.readline()
						var = replace_comments(line).strip()
						table = var.split()
						if not table:
							continue
						else:
							for n in range(len(table)):	
								table[n] = float(table[n])
							# print table
							ListDefinitions[map_entry].append(table)
							print ListDefinitions[map_entry]


			elif "<TABLE>" in peek(foo):
				table = trim(foo.readline(), "TABLE")
				table = table.split()
				ListDefinitions[map_entry] = list()
				for n in range(len(table)):
					table[n] = float(table[n])
				ListDefinitions[map_entry].append(table)
				print ListDefinitions[map_entry]


	print variablesDict
	print ListDefinitions
>>>>>>> 18f5f8edf1b26e8df2db3ae770c02ac919b92a8e
	
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