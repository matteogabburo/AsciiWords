#!/bin/python3

import sys
import ascii_word as aw


def main(args):
    text = 'hello, world!'
    if len(args) > 1:
        text = args[1]
    symbol = '$'
    background = ' '
    n_spaces = 1

    print('Normal\n')
    s = aw.set_str(text, n_spaces)
    aw.print_s(s, symbol, background)

    print('\nItalic (to right)\n')
    s_it_r = aw.to_italic(s)
    aw.print_s(s_it_r, symbol)

    print('\nItalic (to left)\n')
    s_it_l = aw.to_italic(s, to_right=False)
    aw.print_s(s_it_l, symbol)

    print('\nAdd header\n')
    s_header = aw.add_sequence_header(s, '>> ')
    aw.print_s(s_header, symbol)

    print('\nAdd trailer\n')
    s_trailer = aw.add_sequence_trailer(s, ' <<')
    aw.print_s(s_trailer, symbol)

    print('\nAdd on bottom (1 line)\n')
    s_under1 = aw.add_on_bottom(s, '=')
    aw.print_s(s_under1, symbol)

    print('\nAdd on bottom (3 lines)\n')
    s_under3 = aw.add_on_bottom(s, '\n=\n=')
    aw.print_s(s_under3, symbol)

    print('\nAdd on top (1 lines)\n')
    s_on1 = aw.add_on_top(s, '=')
    aw.print_s(s_on1, symbol)

    print('\nAdd on top (3 lines)\n')
    s_on3 = aw.add_on_top(s, '=\n=\n')
    aw.print_s(s_on3, symbol)


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv))
    except (KeyboardInterrupt, SystemExit):
        print('\nBye...')
