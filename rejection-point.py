#!/usr/bin/env python3
"""
Rejection Point
Usage:
    rejection-point.py find <patch> <goodRev> <badRev> <repo>

Options:
    -h --help           Show this screen
"""
from docopt import docopt
import os

# This tool finds the first version that a patch fails to apply cleanly within a commit range.

def git(options):
    return f'cd {options["<repo>"]} && git {options.vcsFlags}'

# Checkout VCS revision
def checkout_revision_git(options, revision):
    co_cmd = f'{git(options)} co {revision}'
    if os.system(co_cmd) != 0:
        print("Checkout failed!")
# Bisect a commit range
def bisect_range_git(options):
    bisect_cmd = f'{git(options)} bisect start {options["<badRev>"]} {options["<goodRev>"]}'
    if os.system(bisect_cmd) != 0:
        print("Bisect failed!")
        stop_bisect_range_git(options)
# Mark a bisection point as good or bad
def bisect_mark(options, is_good):
    bisect_cmd = f'{git(options)} bisect bad'
    if is_good:
        bisect_cmd = f'{git(options)} bisect good'
    if os.system(bisect_cmd) != 0:
        print("Bisect mark failed!")
# Halt bisecting and restore tree
def stop_bisect_range_git(options):
    stop_bisect_cmd = f'{git(options)} bisect reset'
    if os.system(stop_bisect_cmd) != 0:
        print("Reset after bisect failed")
# Apply patch
def can_apply_patch_git(options):
    pass
# Remove applied patch
def clean_checkout_git(options):
    pass

if __name__ == '__main__':
    options = docopt(__doc__, version='Rejecton Point 1.0')
    options["vcsFlags"] = "--no-pager"
    print(options)
    # Check that the patch can be applied to the end of the revision set
    checkout_revision_git(options, options["<badRev>"])
    if can_apply_patch_git(options):
        print("Patch can be successfully applied to range!")
        return 0
    # Check that the patch can apply to the base of the revision set
    if !can_apply_patch_git(options, options["<goodRev>"])
        print("Patch can not be applied to base revision!")
        return 1
    # Start a bisection
    bisect_range_git(options)
    while can_apply_patch_git(options):
        bisect_mark()
    stop_bisect_range_git(options)
