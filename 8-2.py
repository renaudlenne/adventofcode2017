#!/usr/bin/python
import sys
import re
from collections import defaultdict

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    filepath = sys.argv[1]
    values = defaultdict(int)
    highest_value_ever = 0
    with open(filepath) as fp:
        p = re.compile('(\w+) (inc|dec) (-?\d+) if (\w+) ([^ ]+) (-?\d+)')
        for line in fp:
            m = p.match(line)
            if m:
                var, action, action_value, compare_var, comparator, compare_value = m.groups()
                action_value = int(action_value)
                compare_value = int(compare_value)
                if eval("values['%s'] %s %d" % (compare_var, comparator, compare_value)):
                    if action == 'inc':
                        values[var] += action_value
                    else:
                        values[var] -= action_value
                    if values[var] > highest_value_ever:
                        highest_value_ever = values[var]
    print(highest_value_ever)
