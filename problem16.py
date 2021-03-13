class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums_len = len(nums)
        diff = 2**31 - 1
        for i in range(nums_len - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = nums_len - 1
            print("i", i)
            while (low < high):
                value = nums[i] + nums[low] + nums[high]
                
                if abs(target - value) < abs(diff):
                    diff = target - value
                if value > target:
                    high -= 1
                else:
                    low += 1
                
        
        return target - diff
