class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        x = str(x)
        str_len = len(x)
        mid = str_len // 2
        result = False

        if str_len % 2 == 0:
            return self.helper_func(x, str_len, mid-1, mid)
        else:
            return self.helper_func(x, str_len, mid - 1, mid + 1)
        

            
    
    def helper_func(self, x, str_len, i, j):

        while i >= 0 and j < str_len: 
            if x[i] != x[j]:   
                return False
            else:
                i = i - 1
                j = j + 1
                
        return True 
