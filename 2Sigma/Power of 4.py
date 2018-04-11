"""// - power of four
// 解法1 bool isPowerOfFour(int num) {
        return !(num & (num -1)) &&  // power of 2
(num % 3 == 1); // 3n + 1 }
"""

def isPowerOfFour(num):
    return ((num & (num - 1)) == 0) and (num % 3 == 1)



def ispower(n, base):

    if n == base:
        return True

    if base == 1:
        return False

    temp = base

    while (temp <= n):
        if temp == n:
            return True
        temp *= base

    return False

def is_power2(num):

	'states if a number is a power of two'

	return num != 0 and ((num & (num - 1)) == 0)
