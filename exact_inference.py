# returns the distribution over x
def enumeration-ask(X, e, bn):
	Q_X = {}
	for x in bn.vars_dict[X]:
		e_x = e
		e_x[X] = x
		Q_X[x] = enumeration-all(bn.vars_dict, bn.vars_dict.keys(), e_x)
	return normalize(Q_x)
	
def enumeration-all(vars_dict, vars, e):
	if vars == None:
		return 1.0
	
	Y = vars[0]
	if Y in e:
		return P(Y, e[Y]) * enumeration-all(vars_dict, vars[1:], e)
	else:
		sum = 0
		for y in vars_dict[Y]:
			e_y = e
			e_y[Y] = y
			sum += P(Y, y) * enumeration-all(vars_dict, vars[1:], e_y)
		return sum