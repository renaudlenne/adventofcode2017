#!/usr/bin/python
import sys
from collections import Counter

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    filepath = sys.argv[1]
    graph = dict()

    # Construct the graph
    with open(filepath) as fp:
        for line in fp:
            parts = line.split(' -> ')
            node = parts[0].split(' ')[0].strip()
            if len(parts) > 1:
                children = [child.strip() for child in parts[1].split(', ')]
            else:
                children = []
            graph[node] = children


    # Find its root
    node = graph.iterkeys().next()
    while True:
        parents = [n for n in graph if node in graph[n]]
        if len(parents) == 0:
            break
        node = parents[0]

    print(node)
