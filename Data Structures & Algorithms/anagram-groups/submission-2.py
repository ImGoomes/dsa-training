class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = defaultdict(str)
        counter = 0

        for item in strs:
            key = ''.join(sorted(item))
            if key in seen:
                seen.get(key)
                res[seen.get(key)].append(item)
            else:
                res.append([item])
                seen[key] = counter
                counter += 1
        
        return res

        