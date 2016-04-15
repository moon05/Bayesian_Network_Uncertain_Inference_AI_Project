from random import randint

#returns the normalized distribution of P(X | e)
def gibbs_ask(X, e, bn, NSample):
	N = [0] * len(bn.vars_dict[X])
	Z = {}
	x = []
	for var in e:
		x.append(e[var])
	for var in bn.vars_dict:
		if var not in e:
			randvar = randint(0, len(bn.vars_dict[var])-1)
			Z[var] = bn.vars_dict[var][randvar]
	for j in range(NSample):
		for z in Z:
			for var in bn.mb(z):
				randvar = randint(0,len(bn.vars_dict[var])-1)
				e[var] = bn.vars_dict[var][randvar]
			randvar = randint(0,len(bn.vars_dict[z])-1)
			e[z] = bn.vars_dict[z][randvar]
			x.append(bn.P(z, e, bn.mb(z)))
			del e[z]
			for n in def_dict:
				for i in range(len(def_dict[n])):
					if def_dict[n][i] in x:
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
	return (X, e, gibbs_ask(X, e, bn, NSample))