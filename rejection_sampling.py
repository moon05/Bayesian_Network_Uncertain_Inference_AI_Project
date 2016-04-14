from random import randint
import bayesian_network

#Prior-Sample function that is used in RejectionSampling
#returns a list of Probabilty
def prior_sample(bn):
	event = list()
	for X in bn.vars_dict:
		e = {}
		pars = bayesian_network.parents(X)
		# print "Var:" + X
		print ("Parents %s" % str(pars))
		for var in pars:
			print "Printing var"
			# print var
			randvar = randint(0,len(bn.vars_dict[var])-1)
			# print randvar
			e[var] = bn.vars_dict[var][randvar]
			# print e
			print "loop end"
		randvar = randint(0,len(bn.vars_dict[var])-1)
		e[X] = bn.vars_dict[X][randvar]
		event.append(bn.P(X, e, bn.vars_dict[X].index(e[X])))

	return event


def rejection_sample(X, e, bn, NSample):
	print "Inside rejection"
	N = [0]* len(bn.vars_dict[X])
	print X
	parent_of_X = bayesian_network.parents(X)
	print bn.vars_dict
	print bn.defs_dict[(X, parent_of_X)]
	
	for j in range(NSample):
		X_list = prior_sample(bn)
		print "Printing X_list"
		print X_list
		boolean = True
		vars_dict = bn.vars_dict.keys()
		for in in range()
		for i in range(len(vars_dict)):
			print "Printing e vars dict i"
			print e[vars_dict[i]]
			if e[vars_dict[i]] != X_list[i]:
				boolean = False
				print "Boolean became false"
				break
		print "Printing N before Boolean"
		print N
		if boolean:
			for i in range(len(X_list)):
				print i
				N[i] = (X_list[i] + 1)
		else:
			boolean = True
	print N
	return bn.normalize(N)


