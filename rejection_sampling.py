from random import randint
import bayesian_network

#Prior-Sample function that is used in RejectionSampling
#returns a list of Probabilty
def prior_sample(bn):
	event = list()
	for X in bn.vars_dict:
		e = {}
		pars = bayesian_network.parents(X)
		for var in pars:
			randvar = randint(0,len(bn.vars_dict[var])-1)
			e[var] = bn.vars_dict[var][randvar]
		randvar = randint(0,len(bn.vars_dict[X])-1)
		e[X] = bn.vars_dict[X][randvar]
		event.append(bn.P(X, e, bn.vars_dict[X].index(e[X])))
	return event

def rejection_sample(X, e, bn, NSample):
	N = [0]* len(bn.vars_dict[X])
	parents = bayesian_network.parents(X)
	def_dict = bn.defs_dict[(X, parents)]
	
	for j in range(NSample):
		X_list = prior_sample(bn)
		for n in def_dict:
			for i in range(len(def_dict[n])):
				if def_dict[n][i] in X_list:
					N[i] += 1
	return bn.normalize(N)
	
def parse(bn, args):
	argc = len(args)
	if argc < 2 or argc % 2 == 1:
		print "Usage: <SamplingLimit> <query> [<given> <assignment>]*"
		return None
	NSample = int(args[0])
	X = args[1]
	e = {}
	i = 2
	while i < argc:
		e[args[i]] = args[i+1]
		i += 2
	return (X, e, rejection_sample(X, e, bn, NSample))