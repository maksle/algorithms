#!/usr/bin/env python

# Kosaraju's algorithm to find strongly connected components

# graph = {vertex: (inbound edges, outbound edges)} (could have used a list to
# be consistent)
# vertex = an index digit
# edge = a tuple of the vertices incident on the key vertex
graph = {0: ((3,), (6,)),
         1: ((7,), (4,)),
         2: ((5,), (8,)),
         3: ((6,), (0,)),
         4: ((1,), (7,)),
         5: ((8,), (2,7)),
         6: ((0,), (3,8)),
         7: ((4,5), (1,)),
         8: ((6,2), (5,))}

# number of nodes processed so far for first pass
t = -1

# current source vertex for leaders in 2nd pass
source = None

leader = [None for i in range(0,9)]
order = [None for i in range(0,9)]

def dfs(g, v, p):
    """
    g -> graph
    v -> vertex to expand
    p -> pass number (must be 1 or 2)
    """
    global t
    explored.append(v)
    if p == 2:
        leader[v] = source # only relevant in 2nd pass
    for i in graph[v][p-1]:
        if i not in explored:
            dfs(g, i, p)
    if p == 1:
        t += 1
        order[v] = t

# first pass
explored = []
for v in range(8,-1,-1):
    if v not in explored:
        dfs(graph, v, 1)

# 2nd pass
explored = []
for i in range(8,-1,-1):
    nextv = order.index(i)
    if nextv not in explored:
        source = nextv
        dfs(graph, nextv, 2)

# print sccs
from collections import defaultdict
sccs = defaultdict(list)
for node, leadernode in list(enumerate(leader)):
    sccs[leadernode].append(node)

for scc in sccs:
    print "scc:", sccs[scc]
