#!/usr/bin/python
import sys


class Firewall:
    def __init__(self, size):
        self.size = size
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

    severity = 0
    for i in range(max(firewalls.keys())+1):
        if i in firewalls.keys():
            fw = firewalls[i]
            if fw.position == 0:
                severity += i*fw.size
        for fw in firewalls.values():
            fw.move()

    print(severity)
