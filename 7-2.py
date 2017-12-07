#!/usr/bin/python
import sys
from collections import Counter

graph = dict()


class Disc:
    def __init__(self, name, weight, children=None):
        if children is None:
            children = []
        self.name = name
        self.weight = weight
        self.children = children

    def total_weight(self):
        return self.weight + sum([graph[c].total_weight() for c in self.children])

    def is_balanced(self):
        if len(self.children) == 0:
            return True
        return all(graph[c].total_weight() == graph[self.children[0]].total_weight() for c in self.children)

    def unbalanced_child(self):
        for c in self.children:
            c_node = graph[c]
            if not c_node.is_balanced():
                if len(c_node.children) > 0:
                    c_unbalanced = c_node.unbalanced_child()
                    return c_unbalanced if c_unbalanced else c
                else:
                    return c


if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    filepath = sys.argv[1]

    # Construct the graph
    with open(filepath) as fp:
        for line in fp:
            parts = line.split(' -> ')
            node_def = parts[0]
            split_def = node_def.split(' ')
            node = Disc(
                    split_def[0].strip(),
                    int(split_def[1].strip()[1:-1]),
                    [child.strip() for child in parts[1].split(', ')] if len(parts) > 1 else []
            )
            graph[node.name] = node

    # Find the first unbalanced node
    node_name = graph.iterkeys().next()
    while graph[node_name].is_balanced():
        parents = [n for n in graph if node_name in graph[n].children]
        node_name = parents[0]
    unbalanced_parent = graph[graph[node_name].unbalanced_child()]

    # Find the weight difference
    weights = Counter([graph[c].total_weight() for c in unbalanced_parent.children]).most_common(2)
    correct_weight = weights[0][0]
    wrong_weight = weights[1][0]
    weight_diff = correct_weight-wrong_weight
    for c in unbalanced_parent.children:
        node = graph[c]
        if node.total_weight() == wrong_weight:
            print(node.weight+weight_diff)
            break
