from random import randint

#returns the distribution
def prior_sample(bn):
	event = list()
	for X in bn.vars_dict:
		e = {}
		pars = bn.parents(X)
		for var in pars:
			randvar = randint(0,len(bn.vars_dict[var])-1)
			e[var] = bn.vars_dict[var][randvar]
		randvar = randint(0,len(bn.vars_dict[X])-1)
		e[X] = bn.vars_dict[X][randvar]
		event.append(bn.P(X, e, pars))
	return event

#returns the normalized distribution of P(X | e)
def rejection_sample(X, e, bn, NSample):
	N = [0]* len(bn.vars_dict[X])
	parents = bn.parents(X)
	def_dict = bn.defs_dict[(X, parents)]
	
	for j in range(NSample):
		X_list = prior_sample(bn)
		for n in def_dict:
			for i in range(len(def_dict[n])):
				if def_dict[n][i] in X_list:
					N[i] += 1
	return bn.normalize(N)

#parse the input and run the algorithm
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