#!/usr/bin/python
import sys
from collections import Counter

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    filepath = sys.argv[1]
    steps = 0
    first_seen_at_idx = 0
    history = []
    with open(filepath) as fp:
        banks = fp.readlines()[0].split("\t")
        banks = [int(x.strip()) for x in banks]

        while banks not in history:
            steps += 1
            history.append(banks)
            banks = list(banks)
            m = max(banks)
            max_idx = [idx for idx, value in enumerate(banks) if value == m][0]
            max_val = banks[max_idx]
            banks[max_idx] = 0
            for i in range(max_idx+1, max_idx+1+max_val):
                banks[i % len(banks)] += 1

        first_seen_at_idx = [idx for idx, value in enumerate(history) if value == banks][0]

    print len(history) - first_seen_at_idx
