from random import uniform

#returns the normalized distribution of P(X | e)
def gibbs_ask(X, e, bn, NSample):
	N = [0] * len(bn.vars_dict[X])
	Z = {}
	for var in bn.vars_dict:
		if var not in e:
			Z[var] = bn.vars_dict[var][0]
	for j in range(NSample):
		for Zi in bn.topological_sort(Z.keys()):
			x = []
			for i in range(len(bn.vars_dict[Zi])):
				e[Zi] = bn.vars_dict[Zi][i]
				x[i] = bn.P_mb(Zi, e)
			normalized = bn.normalized(x)
			index = uniform(0.0, 1.0)
			temp = 0.0
			for i in range(len(normalized)):
				if index in range(temp, normalized[i]+1):
					index = i
					break
				temp = normalized[i]
			N[index] += 1
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