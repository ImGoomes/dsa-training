class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        curr_count = 0
        

        if len(nums) == 0:
            return max_count
        
        nums.sort()
        last = nums[0]

        for i in range(len(nums)): 
            if i > 0:
                last = nums[i - 1]

                if last != nums[i]:
                    if last == (nums[i] - 1):
                        curr_count += 1
                    else:
                        if curr_count > max_count: 
                            max_count = curr_count
                        curr_count = 1
            else:
                curr_count = 1

        if curr_count > max_count: 
            max_count = curr_count

        return max_count