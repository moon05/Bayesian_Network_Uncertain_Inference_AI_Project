from random import randint
import bayesian_network

#Prior-Sample function that is used in RejectionSampling
#returns a list of Probabilty
def prior_sample(bn):
	event = list()
	for X in bn.vars_dict:
		e = {}
		pars = bayesian_network.parents(X)
		# print ("Parents %s" % str(pars))
		for var in pars:
			randvar = randint(0,len(bn.vars_dict[var])-1)
			e[var] = bn.vars_dict[var][randvar]

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
	def_dict = bn.defs_dict[(X, parent_of_X)]
	
	for j in range(NSample):
		X_list = prior_sample(bn)
		print "Printing X_list"
		print X_list
		boolean = True
		vars_dict = bn.vars_dict.keys()
		for n in (def_dict):
			print n
			print def_dict
			print "Printing e vars dict i"
			for i in range(len(def_dict[n])):
				print X_list
				if def_dict[n][i] in X_list:
					print "Matched"
					N[i] += 1

	print N
	return bn.normalize(N)
	
def parse(bn, args):
	argc = len(args)
	if argc < 2 or argc % 2 == 1:
		print "Usage: <SamplingLimit> <query> [<given> <assignment>]*"
		return None
	N = args[0]
	X = args[1]
	e = {}
	i = 2
	while i < argc:
		e[args[i]] = args[i+1]
		i += 2
	return rejection_sample(X, e, bn, NSample)


