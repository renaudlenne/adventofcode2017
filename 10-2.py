#!/usr/bin/python
import sys
from functools import reduce

def dense_hash(sparse_hash):
    for x in range(0, 256, 16):
        chunk = sparse_hash[x:x+16]
        yield reduce(lambda a, b: a ^ b, chunk)

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print('Syntax : %s <input>' % sys.argv[0])
        exit(1)

    filepath = sys.argv[1]
    with open(filepath) as fp:
        instructions = [ord(c) for c in fp.readlines()[0].strip()] + [17, 31, 73, 47, 23]
    circle = list(range(256))
    position = 0
    skip = 0
    for round in range(64):
        for instruction in instructions:
            if position+instruction <= len(circle):
                circle[position:position+instruction] = reversed(circle[position:position+instruction])
            else:
                nb_at_start = position+instruction-len(circle)
                nb_at_end = instruction-nb_at_start
                reversed_chunk = list(reversed(circle[-nb_at_end:] + circle[:nb_at_start]))
                circle[-nb_at_end:] = reversed_chunk[:nb_at_end]
                circle[:nb_at_start] = reversed_chunk[-nb_at_start:]
            position = (position + instruction + skip) % len(circle)
            skip += 1

    hash = "".join(["%02x" % x for x in dense_hash(circle)])
    print(hash)
