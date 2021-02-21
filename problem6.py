class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        cycle = 2 * numRows - 2
        n = len(s)
        res = [] 
        for i in range (numRows):
            for j in range (0, n, cycle):
                if j + i >= n:
                    break;
                res.append(s[j + i])
                if i != 0 and i != numRows - 1 and j + cycle  - i < n:
                    res.append(s[j + cycle - i])
        
        return ''.join(res)
