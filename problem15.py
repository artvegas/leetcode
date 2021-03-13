class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        nums_len = len(nums)
        for i in range(nums_len - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = nums_len - 1
            lookup = 0 - (nums[i])
            while (low < high):
                value = nums[low] + nums[high]
                if value == lookup:
                    res.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -=1
                elif value > lookup:
                    high -= 1
                else:
                    low += 1
        
        return res
