class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        if len(nums) == 0: 
            return answer

        for i in range(len(nums)):
            x = 0
            m = 1
            while x < len(nums):
                if x != i:
                    m = m * nums[x]

                if x == len(nums) - 1:
                    answer.append(m)
                
                x += 1
        
        return answer


                