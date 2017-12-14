#!/usr/bin/python
import sys
from functools import reduce
from binascii import a2b_hex

def knot_hash(str):
    instructions = [ord(c) for c in str.strip()] + [17, 31, 73, 47, 23]
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
    return hash


def dense_hash(sparse_hash):
    for x in range(0, 256, 16):
        chunk = sparse_hash[x:x+16]
        yield reduce(lambda a, b: a ^ b, chunk)

def create_matrix(base_hash_name):
    for i in range(128):
        line_hash = knot_hash("%s-%d" % (base_hash_name, i))
        bin_hash = a2b_hex(line_hash)
        yield "".join([bin(bs)[2:].zfill(8) for bs in bin_hash])


def neighbors(x, y):
    if x > 0:
        yield (x-1, y)
    if y > 0:
        yield (x, y-1)
    if x < 127:
        yield (x+1, y)
    if y < 127:
        yield (x, y+1)

def visit(matrix, x, y):
    if matrix[x][y] == '1':
        matrix[x] = matrix[x][:y] + '-' + matrix[x][y+1:]
        for nx, ny in neighbors(x, y):
            visit(matrix, nx, ny)

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print('Syntax : %s <input>' % sys.argv[0])
        exit(1)

    base_hash_name = sys.argv[1]
    rows = list(create_matrix(base_hash_name))
    nb_groups = 0
    for row in range(128):
        for col in range(128):
            if rows[row][col] == '1':
                nb_groups += 1
                visit(rows, row, col)

    print(nb_groups)
