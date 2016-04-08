import os

variablesDict = {}
ListDefinitions = {}

# [{'A':[[.011,.99]]}, {'B':[[1223,123213]]}, {(A|B,E):[[0.95 ,0.05],[0.94,0.06],[0.29 ,0.71],[0.001,0.999]]}]
#


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
			a = line
			print a
			var = line.strip()
			print var
			name = var.replace("<NAME>","").replace("</NAME>","")
			print name
			variablesDict[name] = []
			while "<OUTCOME>" in peek(foo):
				print "Collecting values"
				line = foo.readline()
				var = line.strip()
				outcome = var.replace("<OUTCOME>","").replace("</OUTCOME>","")
				print outcome
				variablesDict[name].append(outcome)

		if "<DEFINITION" in line:
			print "Passed the variable tag"
			continue

		if "<FOR>" in line:
			print "Collectiing table"
			a = line
			print a
			var = line.strip()
			print var
			query = var.replace("<FOR>",""),replace("</FOR>","")
			print query





	print variablesDict

currentPath = os.getcwd()
parser(currentPath+'/'+"aima-alarm.xml")
