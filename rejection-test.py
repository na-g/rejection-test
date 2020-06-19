#!/usr/bin/env python3
"""
rejection-test
Test a patch set to see if it will apply cleanly. It is suitable for use
with `git bisect run`.
Usage:
    rejections-test -p <level> <patch>...

Options:
    -p        Number of path segments to strip
    -h --help Show this screen
"""
from docopt import docopt
from os import system
from sys import exit

def can_apply_patches(options):
    for patch in options["<patch>"]:
        if system(f'git --no-pager apply -p {options["<level>"]} {patch}') != 0:
            clean_checkout(options)
            print(f'\nᚖ Applied patch {patch} ᚖ\n')
            return False
    clean_checkout(options)
    print(f'\nᚚ Failed to apply patch {patch} ᚚ\n')
    return True

def clean_checkout(options):
    system(f'git clean -f -d')
    system(f'git checkout -- .')

def main():
    options = docopt(__doc__, version='Rejection Test 1.0')
    if can_apply_patches(options):
        exit(0)
    else:
        exit(1)
if __name__ == '__main__':
    main()