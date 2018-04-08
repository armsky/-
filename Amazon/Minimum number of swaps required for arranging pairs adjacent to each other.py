"""
There are n-pairs and therefore 2n people. everyone has one unique number ranging
from 1 to 2n. All these 2n persons are arranged in random fashion in an Array of
size 2n. We are also given who is partner of whom. Find the minimum number of
swaps required to arrange these pairs such that all pairs become adjacent to each
other.

Example:

Input:
n = 3
pairs[] = {1->3, 2->6, 4->5}  // 1 is partner of 3 and so on
arr[] = {3, 5, 6, 4, 1, 2}

Output: 2
We can get {3, 1, 5, 4, 6, 2} by swapping 5 & 6, and 6 & 1
"""
"""
1) If first and second elements are pair, then simply recur
   for remaining n-1 pairs and return the value returned by
   recursive call.

2) If first and second are NOT pair, then there are two ways to
   arrange. So try both of them return the minimum of two.
   a) Swap second with pair of first and recur for n-1 elements.
      Let the value returned by recursive call be 'a'.
   b) Revert the changes made by previous step.
   c) Swap first with pair of second and recur for n-1 elements.
      Let the value returned by recursive call be 'b'.
   d) Revert the changes made by previous step before returning
      control to parent call.
   e) Return 1 + min(a, b)
   """

def minSwaps(pairs, a):


def helper():
