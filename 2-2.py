#!/usr/bin/python
from __future__ import division
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
            el1 = 0
            el2 = 0
            elems = line.split()
            for idx1, elem in enumerate(elems):
                matches = (int(other) for idx2, other in enumerate(elems) if
                           idx2 != idx1 and (int(other) / int(elem)).is_integer())
                for m in matches:
                    el1 = int(elem)
                    el2 = m
            if el1 > 0:
                checksum += int(el2 / el1)

    print(checksum)
