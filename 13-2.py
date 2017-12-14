#!/usr/bin/python
import sys
from itertools import cycle, islice

def try_passing(firewalls, delay, list_size, fw_sizes):
    for fw in firewalls.values():
        while True:
            if next(fw) == 0:
                break
    for idx, fw in firewalls.items():
        list(islice(fw, delay % fw_sizes[idx]))
    for i in range(list_size):
        for idx, fw in firewalls.items():
            nxt = next(fw)
            if i == idx and nxt == 1:
                return True
    return False


if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print('Syntax : %s <input>' % sys.argv[0])
        exit(1)

    filepath = sys.argv[1]
    firewalls = dict()
    fw_sizes = dict()
    with open(filepath) as fp:
        for line in fp:
            parts = line.split(': ')
            row = int(parts[0].strip())
            size = int(parts[1].strip())
            lst = list(range(size))+list(range((size-2)*-1, 0))
            firewalls[row] = cycle(lst)
            fw_sizes[row] = len(lst)
    list_size = max(firewalls.keys()) + 1

    delay = 0
    while try_passing(firewalls, delay, list_size, fw_sizes):
        if delay % 10000 == 0:
            print(delay)
        delay += 1
    print(delay)
