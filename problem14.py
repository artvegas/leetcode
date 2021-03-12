class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        prefix_length = len(prefix)
        index = 1
        while index < len(strs):
            if prefix_length == 0:
                return ""
            cur_str = strs[index]
            prefix = prefix[:prefix_length]
            if prefix == cur_str[:prefix_length]:
                index += 1
            else:
                prefix_length -= 1
            
        return prefix
                
