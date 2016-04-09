import os
import re
from decimal import *

variablesDict = {}
ListDefinitions = {}

# [{'A':[[.011,.99]]}, {'B':[[1223,123213]]}, {(A|B,E):[[0.95 ,0.05],[0.94,0.06],[0.29 ,0.71],[0.001,0.999]]}]
#

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
	foo = open(filename,"r")
	print "Name of file: " + filename

	while "<!-- Variables -->" not in foo.readline():
		foo.readline()
	while True:
		line = foo.readline()
		if ("</BIF>" in line):
			break

		if "<!-- Variables -->" in line:
			print "First Variables comment found"
			continue

		if "<VARIABLE" in line:
			print "Passed the variable tag"
			continue

		if "<NAME>" in line:
			print "Collecting variable names"
			name = trim(foo.readline(), "NAME")
			variablesDict[name] = []
			while "<OUTCOME>" in peek(foo):
				print "Collecting values"
				outcome = trim(foo.readline(), "OUTCOME")
				print outcome
				variablesDict[name].append(outcome)

		if "<DEFINITION" in line:
			print "Passed the variable tag"
			continue

		if "<FOR>" in line:
			print "Collecting table"
			map_entry = trim(line, "FOR")
			print map_entry
			
			if "<GIVEN>" in peek(foo):
				while "<GIVEN>" in peek(foo):
					given = trim(foo.readline(), "GIVEN")
					map_entry = map_entry + " " + given
				#map_entry has been updated
				print map_entry
				if "<TABLE>" in peek(foo):
					line = foo.readline()
					ListDefinitions[map_entry] = list()
					while "</TABLE>" not in peek(foo):
						line = foo.readline()
						print line
						var = replace_comments(line).strip()
						print var
						table = var.split()
						print table
						if not table:
							continue
						else:
							print "Printing ListDefinitions"
							print ListDefinitions[map_entry]
							for n in range(len(table)):
								print "Entering in tablemaker"
								table[n] = float(table[n])
							print table
							ListDefinitions[map_entry].append(table)
							print ListDefinitions[map_entry]

			elif "<TABLE>" in peek(foo):
				table = trim(foo.readline(), "TABLE")
				print table
				table = table.split()
				ListDefinitions[map_entry] = list()
				print table
				for n in range(len(table)):
					table[n] = float(table[n])
				print table
				print map_entry
				ListDefinitions[map_entry].append(table)
				print ListDefinitions[map_entry]





	print variablesDict
	print ListDefinitions
	
currentPath = os.getcwd()
parser(currentPath+'/'+"aima-alarm.xml")
