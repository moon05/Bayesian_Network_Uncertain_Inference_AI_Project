from random import randint

#returns the distribution with wieghts
def weighted_sample(bn, e):
	w = 1.0
	x = []
	e_p = e.copy()
	for Xi in bn.topological_sort():
		if Xi in e:
			w *= bn.P(Xi, e[Xi], e_p, bn.parents(Xi))
			x.append(e[Xi])
		else:
			e_p[Xi] = bn.vars_dict[Xi][randint(0, len(bn.vars_dict[Xi])-1)]
			x.append(e_p[Xi])
	return x, w

#returns the normalized distribution of P(X | e)
def likelihood(X, e, bn, NSample):
	W = [0] * len(bn.vars_dict[X])

	parents_of_X = bn.parents(X)
	def_dict = bn.defs_dict[(X, parents_of_X)]
	index = bn.topological_sort().index(X)

	for j in range(NSample):
		x, w = weighted_sample(bn, e)
		W[bn.vars_dict[X].index(x[index])] += w
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