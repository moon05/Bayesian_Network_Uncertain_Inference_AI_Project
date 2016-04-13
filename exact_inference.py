# returns the distribution over x
def enumeration_ask(X, e, bn):
	Q_X = []
	vars = bn.topological_sort()
	e_x = e.copy()
	for x in bn.vars_dict[X]:
		e_x[X] = x
		Q_X.append(enumeration_all(bn, vars, e_x))
	return normalize(Q_X)

#returns the probability considering all assignments to unobserved variables	
def enumeration_all(bn, vars, e):
	if not vars:
		return 1.0
	
	Y = vars[0]
	if Y in e:
		return bn.P(Y, e, bn.vars_dict[Y].index(e[Y])) * enumeration_all(bn, vars[1:], e)
	else:
		sum = 0
		e_y = e.copy()
		for i in range(len(bn.vars_dict[Y])):
			y = bn.vars_dict[Y][i]
			e_y[Y] = y
			sum += bn.P(Y, e_y, i) * enumeration_all(bn, vars[1:], e_y)
		return sum

#normalizes distribution list
def normalize(distribution):
	alpha = 0.0
	for element in distribution:
		alpha += element
	normalized = []
	for i in range(len(distribution)):
		normalized.append(distribution[i] / alpha)
	return normalized