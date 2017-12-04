#!/usr/bin/python
import sys
from collections import defaultdict

values = defaultdict(int)  # Doesn't seem to work when calling from bash...


def sum_neighbours(x, y):
    n1 = values.get((x - 1, y - 1), 0)
    n2 = values.get((x - 1, y), 0)
    n3 = values.get((x - 1, y + 1), 0)
    n4 = values.get((x, y - 1), 0)
    n5 = values.get((x, y + 1), 0)
    n6 = values.get((x + 1, y - 1), 0)
    n7 = values.get((x + 1, y), 0)
    n8 = values.get((x + 1, y + 1), 0)
    return n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8


if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    values = dict()
    target = int(sys.argv[1])
    cur_x, cur_y, sq_size, cur_value = (1, 0, 1, 1)
    cur_value = 1
    values[(0, 0)] = 1
    while cur_value < target:
        cur_value = sum_neighbours(cur_x, cur_y)
        values[(cur_x, cur_y)] = sum_neighbours(cur_x, cur_y)
        if cur_x == sq_size:
            if cur_y == sq_size:
                sq_size += 1
                cur_x += 1
            elif cur_y == sq_size * -1:
                cur_x -= 1
            else:
                cur_y -= 1
        elif cur_y == sq_size * -1:
            if cur_x == sq_size * -1:
                cur_y += 1
            else:
                cur_x -= 1
        elif cur_x == sq_size * -1:
            if cur_y == sq_size:
                cur_x += 1
            else:
                cur_y += 1
        else:
            cur_x += 1
    print cur_value
