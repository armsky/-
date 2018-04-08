class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        re = 1
        while n:
            if n & 1:
                re *= x
            x *= x
            n = n >> 1
        return re        
