#!/usr/bin/python
import sys

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    target = int(sys.argv[1])
    cur_x, cur_y, sq_size = (0, 0, 0)
    for i in range(1, target):
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

    distance = abs(cur_x) + abs(cur_y)
    print "(%d, %d) => %d" % (cur_x, cur_y, distance)
