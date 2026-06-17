class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)): 
            curr = i + 1
            while curr < len(numbers):
                if numbers[i] + numbers[curr] == target: 
                    return [i + 1, curr + 1]

                curr += 1