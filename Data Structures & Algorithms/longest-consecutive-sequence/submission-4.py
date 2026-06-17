class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_count = 1
        curr_count = 1
        nums.sort()

        for i in range(len(nums)): 
            if i > 0 and nums[i-1] != nums[i]:
                if nums[i-1] == (nums[i] - 1):
                    curr_count += 1
                else:
                    if curr_count > max_count: 
                        max_count = curr_count
                    curr_count = 1

        return max(max_count, curr_count) 