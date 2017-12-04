#!/usr/bin/python
import sys
from collections import Counter

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    filepath = sys.argv[1]
    nb_valid = 0
    with open(filepath) as fp:
        for line in fp:
            elems = line.split()
            c = Counter(elems)
            if len(elems) == 1:
                continue  # Only one word, this is not a passphrase
            if c.most_common(1)[0][1] == 1:
                # No repeated word, this is a valid passphrase
                nb_valid += 1

    print(nb_valid)
