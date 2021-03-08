class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        map = ["I", "V", "X", "L", "C", "D", "M"]
        index = 0
        result = ""
        while num != 0:
            digit = num % 10
            if 1 <= digit <= 3:
                for i in range(digit):
                    result = map[index] + result
            
            if digit == 4:
                result = map[index] + map[index + 1] + result
            
            if digit == 5:
                result = map[index + 1] + result
                
            if 6 <= digit <= 8:
                diff = digit - 5
                for i in range(diff):
                    result = map[index] + result
                
                result = map[index + 1] + result
            
            if digit == 9:
                result = map[index] + map[index+2] + result
            
            num = num // 10
            index = index + 2
        
        return result
            
