class Solution(object):
    def romanToInt(self, s):
        s = s[::-1]
        dic = {'I': [1,0], 'V': [5,1], 'X': [10,2], 'L': [50,3], 'C': [100,4], 'D': [500,5], 'M': [1000,6]}
        result = dic[s[0]][0]
        for i in range(len(s) - 1):
            if dic[s[i]][1] > dic[s[i+1]][1]: 
                result -= dic[s[i+1]][0]
            else:
                result += dic[s[i+1]][0]
        return result
