#!/usr/bin/python
import sys


class Firewall:
    def __init__(self, size):
        self.size = size
        self.reset()

    def reset(self):
        self.position = 0
        self._dir = "inc"

    def move(self):
        if self.size == 1:
            return
        if self._dir == "inc":
            if self.position + 1 < self.size:
                self.position += 1
            else:
                self._dir = "dec"
                self.position -= 1
        else:
            if self.position == 0:
                self._dir = "inc"
                self.position += 1
            else:
                self.position -= 1


def try_passing(firewalls, delay):
    for fw in firewalls.values():
        fw.reset()
    for t in range(delay):
        for fw in firewalls.values():
            fw.move()
    for i in range(max(firewalls.keys()) + 1):
        if i in firewalls.keys():
            fw = firewalls[i]
            if fw.position == 0:
                return True
        for fw in firewalls.values():
            fw.move()
    return False


if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print('Syntax : %s <input>' % sys.argv[0])
        exit(1)

    filepath = sys.argv[1]
    firewalls = dict()
    with open(filepath) as fp:
        for line in fp:
            parts = line.split(': ')
            row = int(parts[0].strip())
            size = int(parts[1].strip())
            firewalls[row] = Firewall(size)

    delay = 0
    while try_passing(firewalls, delay):
        delay += 1
    print(delay)
