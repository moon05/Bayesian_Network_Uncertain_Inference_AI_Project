from random import randint

#returns the distribution with wieghts
def weighted_sample(bn,e):
	w = 1
	event = list()
	for X in bn.topological_sort():
		pars = bn.parents(X)
		if X in e:
			w *= bn.P(X, e, bn.parents(X))
		else:
			for var in pars:
				randvar = randint(0,len(bn.vars_dict[var])-1)
				e[var] = bn.vars_dict[var][randvar]
			randvar = randint(0,len(bn.vars_dict[X])-1)
			e[X] = bn.vars_dict[X][randvar]
			event.append(bn.P(X, e, bn.parents(X)))
	return event, w

#returns the normalized distribution of P(X | e)
def likelihood(X, e, bn, NSample):
	W = [0] * len(bn.vars_dict[X])

	parents_of_X = bn.parents(X)
	def_dict = bn.defs_dict[(X, parents_of_X)]

	for j in range(NSample):
		event, w = weighted_sample(bn,e)
		for n in def_dict:
			for i in range(len(def_dict[n])):
				if def_dict[n][i] in event:
					W[i] += 1
	return bn.normalize(W)

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
	return (X, e, likelihood(X, e, bn, NSample))