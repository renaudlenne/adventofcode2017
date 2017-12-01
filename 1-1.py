#!/usr/bin/python
import sys

if __name__=="__main__":
    nb_args = len(sys.argv)
    if nb_args != 2:
        print 'Syntax : %s <input>' % sys.argv[0]
        exit(1)

    init_str = sys.argv[1]
    prev_chr = init_str[-1]
    result = 0
    for i in range(0, len(init_str)):
        cur_chr = init_str[i]
        if cur_chr == prev_chr:
            result += int(cur_chr)
        prev_chr = cur_chr
    print(result)
