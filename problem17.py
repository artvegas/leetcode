class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return ""
            
        maps = {}
        maps['2'] = ['a','b','c']
        maps['3'] = ['d','e','f']
        maps['4'] = ['g','h','i']
        maps['5'] = ['j', 'k', 'l']
        maps['6'] = ['m','n', 'o']
        maps['7'] = ['p', 'q', 'r','s']
        maps['8'] = ['t', 'u','v']
        maps['9'] = ['w', 'x', 'y', 'z']

        options = []
        for digit in digits:
            options.append(maps[digit])

        result = []
        options_len = len(options)
        i = 0
        while i < options_len - 1:
            a_start = 0
            a_end = len(options[i]) - 1
            b_end = len(options[i + 1]) - 1
            new_options = []
            while a_start <= a_end:
                b_start = 0
                while b_start <= b_end:
                    new_options.append(options[i][a_start] + options[i + 1][b_start])
                    b_start += 1
                a_start += 1
            options[i+1] = new_options
            i += 1

        return options[options_len - 1]
    
