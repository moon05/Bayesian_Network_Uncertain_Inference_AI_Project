from random import uniform
from random import randint

#returns the distribution
def prior_sample(bn):
	x = []
	for Xi in bn.topological_sort():
		pars = bn.parents(Xi)
		probs = bn.defs_dict[(Xi, pars)].keys()
		probs = probs[randint(0, len(probs)-1)]
		probs = bn.defs_dict[(Xi, pars)][probs]
		index = get_random_index(bn, probs)
		x.append(bn.vars_dict[Xi][index])
	return x

#returns the normalized distribution of P(X | e)
def rejection_sample(X, e, bn, NSample):
	N = [0] * len(bn.vars_dict[X])
	parents = bn.parents(X)
	def_dict = bn.defs_dict[(X, parents)]
	
	topsort = bn.topological_sort()
	index = topsort.index(X)
	
	for j in range(NSample):
		x = prior_sample(bn)
		#print "x: %s|e: %s" % (x, e)
		#print is_consistent(bn, topsort, x, e)
		if is_consistent(topsort, x, e):
			N[bn.vars_dict[X].index(x[index])] += 1
	return bn.normalize(N)

#checks if the generated event is consistent with the evidence given	
def is_consistent(vars_list, x, e):
	for i in range(len(x)):
		if vars_list[i] in e and x[i] != e[vars_list[i]]:
			return False
	return True

#returns a random index based on the distribution
def get_random_index(bn, probs):
	ranges = []
	temp = 0.0
	rand = uniform(0.0, 1.0)
	sorted_list = sorted(probs, key=float)
	for val in sorted_list:
		ranges.append([temp, val])
		temp = val
	ranges[-1][1] = 1.0
	for i in range(len(sorted_list)):
		if rand >= ranges[i][0] and rand < ranges[i][1]:
			return probs.index(sorted_list[i])
	return -1

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