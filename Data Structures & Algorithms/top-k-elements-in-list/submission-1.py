class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        if len(nums) == 0 or k <= 0:
            return []

        for i in range(len(nums)):
            if nums[i] not in seen: 
                seen[nums[i]] = 1
            else: 
                seen[nums[i]] += 1
        
        return sorted(seen, key=lambda x: seen[x], reverse=True)[:k]