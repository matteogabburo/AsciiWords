#!/bin/python3

import sys
import alphabet as aalph


def print_s(m, symbol='#', background=' '):
    for l in m:
        for c in l:
            if c == 1:
                print(symbol, end='')
            elif c == 0:
                print(background, end='')
            else:
                print(c, end='')
        print('')


def to_italic(s, to_right=True):
    italic = []
    if to_right:
        n_spaces_l = len(s)-1
        n_spaces_r = 0
    else:
        n_spaces_l = 0
        n_spaces_r = len(s)-1
    for l in s:
        italic.append([0 for x in range(n_spaces_l)]
                      + l
                      + [0 for x in range(n_spaces_r)])
        if to_right:
            n_spaces_l -= 1
            n_spaces_r += 1
        else:
            n_spaces_l += 1
            n_spaces_r -= 1
    return italic


def set_str(text, nspaces):
    lines = []
    for c in text:
        if len(c) > 1:
            print('Error: "{}" should be a character'.format(c))
            sys.exit()
        if c not in aalph.alphabet:
            print('Error: char "{}" not yet supported'.format(c))
            sys.exit()
        l_c = aalph.alphabet[c]
        for i in range(len(l_c)):
            while i > len(lines)-1:
                lines.append([])
            for j in range(len(l_c[i])):
                lines[i].append(l_c[i][j])
            for j in range(nspaces):
                lines[i].append(0)
    return lines


def to_pycomment(s):
    return add_sequence_header(s, '# ')


def add_sequence_header(s, seq):
    return [[seq] + l for l in s]


def add_sequence_trailer(s, seq):
    return [l + [seq] for l in s]


def add_under(s, seq):
    to_add = seq.split('\n')
    to_add = [' ' if a == '' else a for a in to_add]
    new_s = s[:]
    len_s = len(new_s[0])
    for i in range(len(to_add)):
        new_l = []
        j = 0
        while j < len_s:
            for c in to_add[i]:
                if j >= len_s:
                    break
                new_l.append(c)
                j += 1
        new_s.append(new_l)
    return new_s


def add_on(s, seq):
    to_add = seq.split('\n')
    to_add = [' ' if a == '' else a for a in to_add]

    new_s = []
    len_s = len(s[0])
    for i in range(len(to_add)):
        new_l = []
        j = 0
        while j < len_s:
            for c in to_add[i]:
                if j >= len_s:
                    break
                new_l.append(c)
                j += 1
        new_s.append(new_l)

    for l in s:
        new_s.append(l)

    return new_s


def main(args):
    text = args[1]
    symbol = '#'
    background = ' '
    n_space = 1

    print('Normal\n')
    s = set_str(text, n_space)
    print_s(s, symbol, background)

    print('\nItalic (to right)\n')
    s_it_r = to_italic(s)
    print_s(s_it_r, symbol)

    print('\nItalic (to left)\n')
    s_it_l = to_italic(s, to_right=False)
    print_s(s_it_l, symbol)

    print('\nSeq header\n')
    s_header = add_sequence_header(s, '# ')
    print_s(s_header, symbol)

    print('\nSeq trailer\n')
    s_trailer = add_sequence_trailer(s, '# ')
    print_s(s_trailer, symbol)

    print('\nAdd under (1 line)\n')
    s_under1 = add_under(s, '#')
    print_s(s_under1, symbol)

    print('\nAdd under (3 lines)\n')
    s_under3 = add_under(s, '\n#\n#')
    print_s(s_under3, symbol)

    print('\nAdd on (1 lines)\n')
    s_on1 = add_on(s, '#')
    print_s(s_on1, symbol)

    print('\nAdd on (3 lines)\n')
    s_on3 = add_on(s, '#\n#\n')
    print_s(s_on3, symbol)


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv))
    except (KeyboardInterrupt, SystemExit):
        print('\nBye...')
