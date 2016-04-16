from random import uniform

from collections import deque
 
 
def kahn_topsort(graph):
	in_degree = { u : 0 for u in graph }     # determine in-degree 
	for u in graph:                          # of each node
		for v in graph[u]:
			in_degree[v] += 1
			
	Q = deque()                 # collect nodes with zero in-degree
	for u in in_degree:
		if in_degree[u] == 0:
			Q.appendleft(u)

	L = []     # list for order of nodes

	while Q:                
		u = Q.pop()          # choose node of zero in-degree
		L.append(u)          # and 'remove' it from graph
		for v in graph[u]:
			in_degree[v] -= 1
			if in_degree[v] == 0:
				Q.appendleft(v)

	if len(L) == len(graph):
		return L
	else:                    # if there is a cycle,  
		return []            # then return an empty list

#returns the normalized distribution of P(X | e)
def gibbs_ask(X, e, bn, NSample):
	N = [0] * len(bn.vars_dict[X])
	Z = {}
	for var in bn.vars_dict:
		if var not in e:
			Z[var] = bn.vars_dict[var][0]
	Z_topsort = []
	for var in bn.topological_sort():
		if var in Z:
			Z_topsort.append(var)
	for j in range(NSample):
		for Zi in Z_topsort:
			x = {}
			print "Zi: %s" % Zi
			for val in bn.vars_dict[Zi]:
				e[Zi] = val
				print "Evidence: %s" % e
				x[val] = bn.P_mb(Zi, e)
			normalized = bn.normalized(x.values()).sort()
			index = uniform(0.0, 1.0)
			temp = 0.0
			val = None
			for element in normalized:
				if index in range(temp, element+1):
					for key, value in x.iteritems():
						if element == value:
							val = key
							break
					if val is not None:
						break
				temp = normalized[i]
			index = bn.vars_dict[Zi].index(val)
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