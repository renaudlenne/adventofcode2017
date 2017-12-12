#!/usr/bin/python
import sys

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print('Syntax : %s <input>' % sys.argv[0])
        exit(1)

    filepath = sys.argv[1]
    graph = dict()
    with open(filepath) as fp:
        for line in fp:
            parts = line.split(' <-> ')
            node = int(parts[0])
            graph[node] = set([int(x.strip()) for x in parts[1].split(',')])

    curr_node = 0
    zero_group = set([0])
    to_visit = graph[curr_node]
    visited = set()
    while len(to_visit) > 0:
        visited.add(curr_node)
        zero_group = zero_group | graph[curr_node]
        curr_node = to_visit.pop()
        to_visit = to_visit | (graph[curr_node] - visited)
    print(len(zero_group))
