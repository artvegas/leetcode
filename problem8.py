class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        sign = 1

        result = 0
        max_int_div = 2147483647 / 10
        
        for i in range(len(s)):
            asci_dec = ord(s[i])
            
            if i == 0 :
                if asci_dec == 45 or asci_dec == 43:
                    sign = 44 - asci_dec
                    i = i + 1
                    continue
                
            if asci_dec < 48 or asci_dec > 57:
                break;
            
            i = i + 1
            if result > max_int_div  or (result == max_int_div  and (asci_dec - 48) > 7):
                return 2147483647 if sign == 1 else -2147483648
            
            result = result * 10 + (asci_dec - 48)
        
        return result * sign
