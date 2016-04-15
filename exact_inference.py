# returns the distribution over x
def enumeration_ask(X, e, bn):
	Q_X = []
	vars_list = bn.topological_sort()
	for x in bn.vars_dict[X]:
		e[X] = x
		Q_X.append(enumeration_all(bn, vars_list, e))
	del e[X]
	return bn.normalize(Q_X)

#returns the normalized distribution of P(X | e)
def enumeration_all(bn, vars_list, e):
	if not vars_list:
		return 1.0

	Y = vars_list[0]
	if Y in e:
		return bn.P(Y, e, bn.parents(Y)) * enumeration_all(bn, vars_list[1:], e)
	else:
		sum = 0.0
		for i in range(len(bn.vars_dict[Y])):
			e[Y] = bn.vars_dict[Y][i]
			sum += bn.P(Y, e, bn.parents(Y)) * enumeration_all(bn, vars_list[1:], e)
		del e[Y]
		return sum

#parse the input and run the algorithm
def parse(bn, args):
	argc = len(args)
	if argc < 1 or argc % 2 == 0:
		print "Usage: <query> [<given> <assignment>]*"
		return None
	X = args[0]
	e = {}
	i = 1
	while i < argc:
		e[args[i]] = args[i+1]
		i += 2
	return (X, e, enumeration_ask(X, e, bn))