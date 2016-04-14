# returns the distribution over x
def enumeration_ask(X, e, bn):
	Q_X = []
	vars_list = bn.topological_sort()
	for x in bn.vars_dict[X]:
		e[X] = x
		Q_X.append(enumeration_all(bn, vars_list, e))
	del e[X]
	return normalize(Q_X)

#returns the probability considering all assignments to unobserved variables	
def enumeration_all(bn, vars_list, e):
	if not vars_list:
		return 1.0
	
	Y = vars_list[0]
	if Y in e:
		return bn.P(Y, e, bn.vars_dict[Y].index(e[Y])) * enumeration_all(bn, vars_list[1:], e)
	else:
		sum = 0.0
		for i in range(len(bn.vars_dict[Y])):
			e[Y] = bn.vars_dict[Y][i]
			sum += bn.P(Y, e, i) * enumeration_all(bn, vars_list[1:], e)
		del e[Y]
		return sum

#normalizes distribution list
def normalize(distribution):
	alpha = 0.0
	for element in distribution:
		alpha += element
	if alpha == 0.0:
		return distribution
	normalized = []
	for i in range(len(distribution)):
		normalized.append(distribution[i] / alpha)
	return normalized