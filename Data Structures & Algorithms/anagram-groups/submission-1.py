class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        left, right = 0, 0
        anagrams = []
        seen = []

        if len(strs) == 0:
            return strs

        while left < len(strs):
            curr = []
            right = left + 1

            if left not in seen:
                curr.append(strs[left])

            while right < len(strs):
                if sorted(strs[left]) == sorted(strs[right]) and right not in seen:
                    curr.append(strs[right])
                    seen.append(right)
            
                right += 1
            left += 1
            if len(curr) > 0:                
                anagrams.append(curr)

        return anagrams