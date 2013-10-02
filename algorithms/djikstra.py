#!/usr/bin/env python

import heapq

# array of [value, nodeid]. index is nodeid
graph = [[(1,1)],
         [(1,0), (5,2), (3,5)],
         [(5,5)],
         [(5,1), (6,4), (1,5)],
         [(2,5), (6,3)],
         [(2,4), (4,0)]]

def djikstra(graph, source):
    nodes = []
    dist = [None for i in xrange(0,len(graph))]
    prev = []

    # heapq doesn't provide decrease-key so we have to add duplicates into the
    # heap and check if it's been minExtracted already at O(1) dict lookup time
    used = {}

    for v in xrange(0,len(graph)) :
        nodes.append((float("inf"), v, None)) # weight, nodeid, prev
        prev.append(None)

    nodes[source] = (0, 0, None)

    heapq.heapify(nodes) # O(log v)

    while len(nodes) > 0:
        w = heapq.heappop(nodes) # O(1)
        w_index = w[1]

        if w_index in used:
            continue
        if w[0] == float("inf"):
            raise Exception('no path exists to source')

        used[w_index] = True
        print "used:", used
        dist[w_index] = w[0]
        prev[w_index] = w[2]

        for weight, node in graph[w_index]:
            if node not in used: # O(1) lookup time
                heapq.heappush(nodes, (w[0]+weight, node, w_index))

    print "distances:", dist
    print "paths:", prev
    return dist, prev

djikstra(graph, 0)

