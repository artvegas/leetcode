class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        rev = 0
        minsize = -sys.maxint - 1
        while x != 0:
            pop = x % 10
            x = x / 10
            if rev > sys.maxsize / 10 or (rev == sys.maxsize / 10 and pop > 7):
                return 0
            if rev < minsize / 10 or (rev == minsize / 10 and pop < -8):
                return 0
            rev = rev * 10 + pop 
        
        return rev
