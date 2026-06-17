class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        if len(s) == 0 and len(t) == 0:
            return False

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1

        for j in range(len(t)):
            if t[j] not in seen:
                return False
            else: 
                seen[t[j]] -= 1
    

        print(seen)
        
        if any(v != 0 for v in seen.values()):
            return False


        return True
