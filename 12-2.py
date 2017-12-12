#!/usr/bin/python
import sys

def group(initial_node):
    curr_node = initial_node
    this_group = set([initial_node])
    to_visit = graph[curr_node]
    visited = set()
    while len(to_visit) > 0:
        visited.add(curr_node)
        this_group = this_group | graph[curr_node]
        curr_node = to_visit.pop()
        to_visit = to_visit | (graph[curr_node] - visited)
    return this_group


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


    nb_groups = 0
    all_visited = set()
    while len(all_visited) < len(graph):
        nb_groups += 1
        next_node = (set(graph.keys()) - all_visited).pop()
        all_visited = all_visited | group(next_node)
    print(nb_groups)
