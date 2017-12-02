#!/usr/bin/python
import sys

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    filepath = sys.argv[1]
    checksum = 0
    with open(filepath) as fp:
        for line in fp:
            elems = line.split()
            head, tail = elems[0], elems[1:]
            min_nb = int(head)
            max_nb = int(head)
            for stri in tail:
                i = int(stri)
                if i < min_nb:
                    min_nb = i
                if i > max_nb:
                    max_nb = i
            diff = max_nb - min_nb
            checksum += diff
    print(checksum)
