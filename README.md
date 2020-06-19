## Rejection Point
This script tests a patch set to see if it will apply cleanly. It is suitable for use
with `git bisect run`, which in turn allows one to know when a patch no longer applies
cleanly. This helps solve the problem of identifying when a fix on a fork will need
manual reapplication when updating the fork from upstream.

### Usage
Warning: this will discard any uncommited changes, so stash or commit your local changes before you attempt a bisection.
Assuming that `rejection-point.py` is in your path, and you have a clean checkout in your target repo:
1. Find a patch that you need to see exactly when in the tree it no longer applied cleanly.
2. Start a bisect on the target git repo with `git bisect start`.
3. Set the "good" revision to the last revision you are sure the patch applied with `git bisect good some_rev`.
4. Set the "bad" revision to a descendant revision of "good" in which the patch doesn't apply with `git bisect bad some_rev`.
5. Run `git bisect run rejection-point.py -pX your.patch` where `X` is the number of path segments to strip from the patch.
6. Bisect will then bisect through the revisions between "good" and "bad", and it will report the first version where the patch no longer applied.
7. Profit
