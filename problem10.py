class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        p_len = len(p)
        s_len = len(s)
        def dp(i, j):
            if (i, j) not in memo:
                if j == p_len:
                    ans = i == s_len
                else:
                    first_match = i < s_len and p[j] in {s[i], '.'}
                    if j + 1 < p_len and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j]= ans
            return memo[i,j]
        
        return dp(0,0)
