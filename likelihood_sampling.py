import bayesian_network
from random import randint

def weighted_sample(bn,e):
	w = 1
	event = list()
	pars = bayesian_network.parents(X)
	for X in bn.vars_dict:
		if X in e:
			w = w * bn.P(X, e, bn.vars_dict[X].index(X))
		else:
			randvar = randint(0,len(bn.vars_dict[var])-1)
			e[X] = bn.vars_dict[X][randvar]
			event.append(bn.P(X, e, bn.vars_dict[X].index(e[X])))
			event.append()

	return event, w

def likelihood(X, e, bn, NSample):
	W = [0] * len(bn.vars_dict)

	parents_of_X = bayesian_network.parents(X)
	def_dict = bn.defs_dict[(X, parents_of_X)]

	for j in range(NSample):
		event, w = weighted_sample(bn,e)
	for everything
