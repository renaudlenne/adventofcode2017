#!/usr/bin/python
import sys

reverse_directions = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

if __name__ == "__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print('Syntax : %s <input>' % sys.argv[0])
        exit(1)

    filepath = sys.argv[1]
    optimized_path = []
    with open(filepath) as fp:
        real_path = [x.strip() for x in fp.readlines()[0].split(',')]
        for direction in real_path:
            if len(direction) == 1:
                reverse = reverse_directions[direction]
            else:
                reverse = "".join([reverse_directions[direction[0]], reverse_directions[direction[1]]])
            if reverse in optimized_path:
                optimized_path.remove(reverse)
            elif len(direction) == 1:
                others = [idx for (idx, c) in enumerate(optimized_path) if reverse in c]
                if len(others) > 0:
                    old_dir = optimized_path.pop(others[0])
                    optimized_path.append(old_dir.replace(reverse, direction))
                else:
                    optimized_path.append(direction)
            else:
                others = [idx for (idx, c) in enumerate(optimized_path) if c in reverse]
                if len(others) > 0:
                    old_dir = optimized_path.pop(others[0])
                    optimized_path.append(direction.replace(reverse_directions[old_dir], old_dir))
                else:
                    others = [idx for (idx, c) in enumerate(optimized_path) if c == reverse[0]]
                    if len(others) > 0:
                        old_dir = optimized_path.pop(others[0])
                        new_dir = old_dir.replace(list(set(old_dir) & set(reverse))[0], '')
                        optimized_path.append(new_dir)
                    else:
                        optimized_path.append(direction)

    print("%d (%s)" % (len(optimized_path), optimized_path))
