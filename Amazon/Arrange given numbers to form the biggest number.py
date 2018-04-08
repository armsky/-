"""
Given an array of numbers, arrange them in a way that yields the largest value.
For example, if the given numbers are {54, 546, 548, 60}, the arrangement
6054854654 gives the largest value. And if the given numbers are
{1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the
largest value.
"""
def compare(a, b):
    if int(a+b) < int(b+a):
        return -1
    else:
        return 1

def printLargest(l):
    a = [str(i) for i in l]
    a.sort(cmp=compare, reverse=True)
    res = ''
    for n in a:
        res += n
    return res
